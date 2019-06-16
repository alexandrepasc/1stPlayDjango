from django.shortcuts import render


def signup(request):
    setattr(request, 'view', 'signup')
    setattr(request, 'breadcrumb', 'Sign up')

    return render(request, 'signup.html')
