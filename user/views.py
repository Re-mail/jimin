from django.shortcuts import render
from .models import Login

def index(request):
    logins = Login.objects.all()
    return render(
        request,
        'user/index.html',
        {
            'logins': logins,
        }
    )
