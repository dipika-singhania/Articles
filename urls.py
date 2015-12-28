from django.conf.urls import url
from . import views

app_name = 'Articles'

urlpatterns = [
	url(r'^$',views.index,name="index"),
	url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^random/$',views.random_generator,name='random'),
	url(r'^nextArticleSet/$',views.nextArticleSet , name="nextArticleSet"),
	url(r'^prevArticleSet/$',views.prevArticleSet , name="prevArticleSet"),
	url(r'^currArticleSet/$',views.currArticleSet , name="currArticleSet"),
]