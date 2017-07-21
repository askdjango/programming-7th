from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.article_list, name='article_list'),
    url(r'^new/$', views.article_new, name='article_new'),
    url(r'^nametag/(?P<company>[a-zA-Z0-9ㄱ-힣]+)/(?P<name>[ㄱ-힣]+)/$', views.nametag, name='nametag'),
    url(r'^(?P<slug>[-\w]+)/$', views.article_detail, name='article_detail'),
]

