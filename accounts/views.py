from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def signup(request):
    setattr(request, 'view', 'signup')
    setattr(request, 'breadcrumb', 'Sign up')
    setattr(request, 'submitName', 'Sign')

    form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})
