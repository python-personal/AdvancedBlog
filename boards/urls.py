from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeListView.as_view(),name='home'),
    path('boards/<int:board_id>/',views.TopicListView.as_view(),name='board_topics'),
    # path('boards/<int:board_id>/', views.TopicListView.as_view(), name='board_topics'),

    path('boards/<int:board_id>/new/',views.new_topics,name='new_topics'),
    path('boards/<int:board_id>/topics/<int:id>/',views.PostListView.as_view(),name='topic_posts'),
    path('boards/<int:board_id>/topics/<int:id>/reply',views.reply_topic,name='reply'),
    # path('boards/new_post/',views.new_posts,name='new_post'),
    path('boards/<int:board_id>/topics/<int:topic_id>/posts/<int:post_id>/edit/',views.PostUpdateView.as_view(),name='edit_post'),


]
