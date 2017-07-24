from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


def post_list(request):
    qs = Post.objects.all()

    query = request.GET.get('query', '')
    if query:
        condition = Q(title__icontains=query) | Q(content__icontains=query)
        qs = qs.filter(condition)

    return render(request, 'blog/post_list.html', {
        'post_list': qs,
        'query': query,
    })


# post_list = ListView.as_view(model=Post)



def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })

