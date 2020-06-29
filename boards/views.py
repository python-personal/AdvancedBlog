from django.shortcuts import render,get_object_or_404,redirect
from . models import *
from . forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.views.generic import UpdateView,ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.decorators import method_decorator
from django.urls import reverse

# Create your views here.

class HomeListView(ListView):
    model = Board
    context_object_name = 'boards'
    template_name = 'boards/home.html'

class TopicListView(ListView):
    model = Topic
    context_object_name = 'topics'
    template_name = 'boards/topics.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        print('hel1')
        kwargs['board'] = self.board
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        print('hel2')
        self.board = get_object_or_404(Board, id=self.kwargs.get('board_id'))
        print(self.board)
        queryset = self.board.topics.order_by('-last_update').annotate(replies=Count('posts') - 1)
        return queryset



@login_required
def new_topics(request,board_id):
    board=get_object_or_404(Board,id=board_id)
    if request.method=='POST':
        form=NewTopicsForm(request.POST)
        if form.is_valid():
            topic=form.save(commit=False)
            topic.board=board
            topic.starter=request.user
            topic.save()
            post=Post.objects.create(message=form.cleaned_data.get('message'),topic=topic,created_by=request.user)
            return redirect('topic_posts',board_id=board.id,id=topic.id)
    else:
        form=NewTopicsForm()
    return render(request,'boards/new_topic.html',{'board':board,'form':form})



class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'boards/topic_posts.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):

        session_key = 'viewed_topic_{}'.format(self.topic.id)  # <-- here
        if not self.request.session.get(session_key, False):
            self.topic.views += 1
            self.topic.save()
            self.request.session[session_key] = True           # <-- until here

        kwargs['topic'] = self.topic
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.topic = get_object_or_404(Topic, board__id=self.kwargs.get('board_id'), id=self.kwargs.get('id'))
        queryset = self.topic.posts.order_by('created_at')
        return queryset



@login_required
def reply_topic(request,board_id,id):
    topic=get_object_or_404(Topic,board_id=board_id,id=id)
    if request.method=='POST':
        form=PostReplyForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.topic=topic
            post.created_by=request.user
            post.save()
            topic_url = reverse('topic_posts', kwargs={'board_id': board_id, 'id': id})
            topic_post_url = '{url}?page={page}#{id}'.format(
                url=topic_url,
                id=post.id,
                page=topic.get_page_count()
            )

            return redirect(topic_post_url)
            # return redirect('topic_posts',board_id=board_id,id=id)
    else:
        form=PostReplyForm()
    return render(request,'boards/reply_topic.html',{'topic':topic,'form':form})

# # function based views
# def new_posts(request):
#     if request.method=='POST':
#         form=PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#         else:
#             form=PostForm()
#         return render(request,'boards/new_post.html',{'form':form})
#
# # class based views where it will extend the View function
# from django.views.generic import View
#
# class NewPostView(View):
#     def render(self, request):
#         return render(request, 'boards/new_post.html', {'form': self.form})
#
#     def post(self, request):
#         self.form = PostForm(request.POST)
#         if self.form.is_valid():
#             self.form.save()
#             return redirect('post_list')
#         return self.render(request)
#
#     def get(self, request):
#         self.form = PostForm()
#         return self.render(request)
# # generic class view are the views which will extends particular class form generic class
#
# from django.views.generic import CreateView
#
# class NewPostView(CreateView):
#     model = Post
#     form_class = PostForm
#     success_url = reverse_lazy('post_list')
#     template_name = 'boards/new_post.html'

@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    fields = ('message', )
    template_name = 'boards/edit_post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    def form_valid(self, form):
        print('inside form dataaaa')
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_at = timezone.now()
        post.save()
        return redirect('topic_posts', board_id=post.topic.board_id, id=post.topic.id)
