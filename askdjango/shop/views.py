from django.shortcuts import get_object_or_404, redirect, render
from .forms import RatingForm
from .models import Shop



def rating_new(request, shop_pk):
    # shop = Shop.objects.get(pk=shop_pk)
    shop = get_object_or_404(Shop, pk=shop_pk)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.shop = shop
            rating.save()
            return redirect('/')  # FIXME
    else:
        form = RatingForm()
    return render(request, 'shop/rating_form.html', {
        'form': form,
    })

