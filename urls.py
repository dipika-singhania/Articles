from django.conf.urls import url
from . import views

app_name = 'Articles'

urlpatterns = [
	url(r'^$',views.index,name="index"),
	url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^random/$',views.random_generator,name='random'),
	url(r'^articleSet/(?P<start_article_id>[0-9]+)/$',views.articleSet , name="articleSet"),
]