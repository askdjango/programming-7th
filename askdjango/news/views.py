from django.shortcuts import get_object_or_404, render
from .models import Article

def article_list(request):
    return render(request, 'news/article_list.html', {
        'article_list': Article.objects.all(),
    })

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'news/article_detail.html', {
        'article': article,
    })

