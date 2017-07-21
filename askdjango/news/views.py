from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm

def article_list(request):
    return render(request, 'news/article_list.html', {
        'article_list': Article.objects.all(),
    })

@login_required
def article_new(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
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


def nametag(request, company, name):
    return HttpResponse('회사 : {}, 이름 : {}'.format(company, name))

