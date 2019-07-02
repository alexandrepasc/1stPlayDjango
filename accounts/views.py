from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, resolve

from .forms import SignUpForm, SignInForm


def signup(request):
    setattr(request, 'view', 'signup')
    setattr(request, 'breadcrumb', 'Sign up')
    setattr(request, 'submitName', 'Sign')

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


#TODO: don't return error to page
def signin(request):
    setattr(request, 'view', 'login')
    setattr(request, 'breadcrumb', 'Log in')
    setattr(request, 'submitName', 'Log in')

    if request.method == 'POST':
        form = SignInForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        nexturl = request.GET['next'] if 'next' in request.GET else ''

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)

            if nexturl is not '':
                return redirect(nexturl)
            else:
                return redirect('home')

    else:
        form = SignInForm()

    return render(request, 'login.html', {'form': form})
