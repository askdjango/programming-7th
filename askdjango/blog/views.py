from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from .models import Post
from .forms import PostForm


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


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/blog/{}/'.format(post.id))
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })

