from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    return HttpResponse('글목록을 보여주겠소.')

def post_detail(request, pk):
    return HttpResponse('{}번 글을 보여주겠소.'.format(pk))

