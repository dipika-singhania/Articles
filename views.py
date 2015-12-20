#!/usr/bin/python
import random
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.core.paginator import Paginator
#!/usr/bin/python
import random
from .models import Article,Category
from django.template import RequestContext, loader

# Create your views here.
def index(request):
	weekdays = ['Monday',"Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
	alreadyPublishedArticles = Article.objects.filter(publication_date__lte=datetime.date.today()).order_by('publication_date').reverse()
	page_size = 4
	paginator = Paginator(alreadyPublishedArticles, page_size)
	page = request.GET.get('page')
	if(page==None):
		page = 1
	try:
	   articlePerPage = paginator.page(page)
	except PageNotAnInteger:
		articlePerPage = paginator.page(1)
	except EmptyPage:
		articlePerPage = paginator.page(paginator.num_pages)
	return render(request, 'Articles/ArticleList.html', 
	{'alreadyPublishedArticles':alreadyPublishedArticles , 'articlePerPage': articlePerPage}
	)
	
	
def detail(request, article_id):
	alreadyPublishedArticles = Article.objects.filter(publication_date__lte=datetime.date.today()).order_by('publication_date').reverse()
	page_size = 4
	paginator = Paginator(alreadyPublishedArticles, page_size)
	page = request.GET.get('page')
	if(page==None):
		page = 1
	try:
	   articlePerPage = paginator.page(page)
	except PageNotAnInteger:
		articlePerPage = paginator.page(1)
	except EmptyPage:
		articlePerPage = paginator.page(paginator.num_pages)
	article_detail = Article.objects.get(id=article_id)
	return render(request, 'Articles/ArticleDetail.html' , {'article_detail':article_detail,'articlePerPage': articlePerPage})

	
def random_generator(request):
	alreadyPublishedArticles = Article.objects.filter(publication_date__lte=datetime.date.today())
	index = random.randrange(0, len(alreadyPublishedArticles))
	article_random = Article.objects.get(id=index)
	return render(request, 'Articles/detailSnippet.html',{'article_random': article_random})

