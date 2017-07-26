from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.shop_list, name='shop_list'),
    url(r'^(?P<pk>\d+)/$', views.shop_detail, name='shop_detail'),
    url(r'^(?P<shop_pk>\d+)/rating/new/$', views.rating_new, name='rating_new')
]

