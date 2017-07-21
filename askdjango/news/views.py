from django.shortcuts import get_object_or_404, redirect, render
from .models import Article
from .forms import ArticleForm

def article_list(request):
    return render(request, 'news/article_list.html', {
        'article_list': Article.objects.all(),
    })

def article_new(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.ip = request.META['REMOTE_ADDR']
            article.save()
            # return redirect('/news/')
            return redirect('news:article_list')
    else:
    #if request.method == 'GET':
        form = ArticleForm()
    return render(request, 'news/article_form.html', {
        'form': form,
    })

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'news/article_detail.html', {
        'article': article,
    })

