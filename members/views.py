from django.http import HttpResponse
from django.shortcuts import render
from .models import PostForm
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    post_form = PostForm.objects.all()
    paginator = Paginator(post_form, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'members/index.html', {'post_form': page_obj})


def detail(request, id):
    post = PostForm.objects.get(id=id)
    return render(request, 'members/detail.html', {'post': post})
