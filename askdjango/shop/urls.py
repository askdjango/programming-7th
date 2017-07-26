from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<shop_pk>\d+)/rating/new/$', views.rating_new, name='rating_new')
]

