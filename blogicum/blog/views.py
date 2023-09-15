from django.shortcuts import render
from django.http import HttpResponse, Http404

from blog.models import Post

def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.all().filter(is_published=True).order_by('title')[:5]
    context = {'post_list': post_list}
    return render(request, template, context)

def post_detail(request, pk):
    template = 'blog/detail.html'
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, template, context)

def category_posts(request, category_slug):
    template = 'blog/category.html'
    post_list = Post.objects.select_related('category').filter(
        is_published=True,
        category__is_published=True,
    ).order_by('category')
    context = {'post_list': post_list}
    return render(request, template, context)
