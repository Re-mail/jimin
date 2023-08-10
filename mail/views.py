from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(
        request,
        'mail/landing.html',
    )

def about(request):
    return render(
        request,
        'mail/about.html',
    )

def login(request):
    return render(
        request,
        'user/index.html',
    )

def signup(request):
    return render(
        request,
        'mail/signup.html',
    )