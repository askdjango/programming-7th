from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.article_list, name='article_list'),
    url(r'^new/$', views.article_new, name='article_new'),
    url(r'^(?P<slug>[-\w]+)/$', views.article_detail, name='article_detail'),
]

