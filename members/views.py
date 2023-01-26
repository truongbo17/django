from django.http import HttpResponse
from django.shortcuts import render
from .models import PostForm


# Create your views here.
def index(request):
    post_form = PostForm.objects.all()
    return render(request, 'members/index.html', {'post_form': post_form})


def detail(request, id):
    post = PostForm.objects.get(id=id)
    return render(request, 'members/detail.html', {'post': post})
