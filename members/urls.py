from django.urls import path

from . import views

app_name = 'members'

urlpatterns = [
    path('', views.index, name='member'),
    path('/<int:id>', views.detail, name='detail'),
]
