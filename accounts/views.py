from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.shortcuts import redirect, render

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


def signin(request):
    setattr(request, 'view', 'login')
    setattr(request, 'breadcrumb', 'Log in')
    setattr(request, 'submitName', 'Log in')

    if request.method == 'POST':
        form = SignInForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')

        # if form.is_valid():
        #     username = request.POST['username']
        #     password = request.POST['password']
        #     print("-----------------------------------------")
        #     user = authenticate(request, username=username, password=password)
        #
        #     if user is not None:
        #         auth_login(request, user)
        #         return redirect('home')
    else:
        form = SignInForm()

    return render(request, 'login.html', {'form': form})
