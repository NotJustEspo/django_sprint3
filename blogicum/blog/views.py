from django.utils import timezone

from django.shortcuts import render, get_object_or_404

from blog.models import Post, Category

query_limit = 5


def base_query():
    query_set = Post.objects.select_related(
        'location',
        'author',
        'category'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now())
    return query_set


def index(request):
    template = 'blog/index.html'
    post_list = base_query()[:query_limit]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    post = get_object_or_404(base_query().filter(
        pk=pk,))
    context = {
        'post': post,
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True)
    post_list = base_query().filter(
        category=category,)
    context = {'category': category,
               'post_list': post_list}
    return render(request, template, context)
