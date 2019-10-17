
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Profile


def homeView(request):
    return render(request, 'base.html', {})


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def profileView(request):
    userprofile = Profile.objects.get(user=request.user)
    context = {
        'userprofile': userprofile
    }
    return render(request, 'profile.html', context)
