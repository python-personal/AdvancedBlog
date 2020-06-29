from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from . forms import SignupForm
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.

def signupview(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # user=form.save()
            # auth_login(request,user)
            return redirect('login')
    else:
        form=SignupForm()
    return render(request,'accounts/signup.html',{'form':form})


class UserUpdateview(UpdateView):
    model=User
    template_name='accounts/my_accounts.html'
    fields=('first_name','last_name','email')
    success_url=reverse_lazy('home')

    def get_object(self):
        return self.request.user
