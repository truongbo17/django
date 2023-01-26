from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('/register', views.Register.as_view(), name='register'),
    path('/login', views.Login.as_view(), name='login'),
    path('/logout', views.logoutUser, name='logout'),
    path('/private', views.privatePage, name='privatePage'),
]
