from typing import Any, Dict
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.views.generic.edit import UpdateView
from .models import Profile
from django.urls import reverse

# Create your views here.

# no need to create new model for users since it's embedded in django

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # form will get all data submitted via Post method
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, your account is created')
            return redirect('login')
    else:
        form = RegisterForm()
        # when just visiting the page, request method is not going to be post, so only the user creation form will be generated
    return render(request,'users/register.html',{'form':form})


@login_required
# added decorator so not logged in viewer can not visit profile.html, by default, Django will redirect the user to login page (redefined in setting)
def profilepage(request):
    return render(request, 'users/profile.html')
