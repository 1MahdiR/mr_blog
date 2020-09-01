from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from .forms import LoginForm, UserRegistrationForm, UserEditForm

# Create your views here.
@login_required
def dashboard(req):
    if req.method == "POST":
        user_form = UserEditForm(instance = req.user, data = req.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance = req.user)

    return render(req, 'account/dashboard.html', {'user_form': user_form})

def register(req):
    if req.method == "POST":
        user_form = UserRegistrationForm(req.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            login(req, new_user)
            return HttpResponseRedirect(reverse('blog:index'))
    else:
        user_form = UserRegistrationForm()
    return render(req, 'account/register.html', {'user_form':user_form})

def user_login(req):
    if req.method == "POST":
        form = LoginForm(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(req, username = cd['username'], password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(req, user)
                    return HttpResponseRedirect(reverse('blog:index'))
                else:
                    return HttpResponse("Disabled Account!")
            else:
                return HttpResponse("Invalid login!")
    else:
        form = LoginForm()
    return render(req, 'account/login.html', {'form':form})

def user_logout(req):
    logout(req)
    return HttpResponseRedirect(reverse('blog:index'))
