from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('about/', views.about),
    path('signup/', views.signup),
    path('', views.landing),
]