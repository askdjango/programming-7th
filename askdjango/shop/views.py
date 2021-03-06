from django.shortcuts import get_object_or_404, redirect, render
from .forms import RatingForm
from .models import Shop


def shop_list(request):
    return render(request, 'shop/shop_list.html', {
        'shop_list': Shop.objects.all(),
    })


def shop_detail(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, 'shop/shop_detail.html', {
        'shop': shop,
    })


def rating_new(request, shop_pk):
    # shop = Shop.objects.get(pk=shop_pk)
    shop = get_object_or_404(Shop, pk=shop_pk)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.shop = shop
            rating.save()
            rating.shop.calc_score()
            return redirect('shop:shop_detail', rating.shop.pk)
    else:
        form = RatingForm()
    return render(request, 'shop/rating_form.html', {
        'form': form,
    })

