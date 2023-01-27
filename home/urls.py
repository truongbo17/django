from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='home'),
    path('upload', views.upload, name='upload'),
    path('saveFile', views.saveFile, name='saveFile'),
    path('uploadMultiple', views.FileFieldFormView.as_view(), name='uploadMultiple'),
]
