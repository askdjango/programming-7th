from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def post_list(request):
    qs = Post.objects.all()
    return render(request, 'blog/post_list.html', {
        'post_list': qs,
    })


def post_detail(request, pk):
    return HttpResponse('{}번 글을 보여주겠소.'.format(pk))

