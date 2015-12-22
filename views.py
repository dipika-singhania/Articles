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
	try:
		article_detail = Article.objects.get(id=article_id)
	except Article.DoesNotExist:
		article_detail = None;
	return render(request, 'Articles/ArticleDetail.html' , {'article_detail':article_detail,'articlePerPage': articlePerPage})
	
def random_generator(request):
	alreadyPublishedArticles = Article.objects.filter(publication_date__lte=datetime.date.today())
	lenFinal = Article.objects.all().order_by('id').last().id
	index = random.randrange(0, lenFinal)
	article_random = Article.objects.get(id=index)
	iter = 0
	while(article_random==None or iter<100):
		index = random.randrange(0, lenFinal)
		try:
			article_random = Article.objects.get(id=index)
			if not(alreadyPublishedArticles.filter(id=index).exists()):
				article_random = None
		except Article.DoesNotExist:
			article=None
		iter += 1
	return render(request, 'Articles/detailSnippet.html',{'article_random': article_random})

def articleSet(request,start_article_id):
	alreadyPublishedArticles = Article.objects.filter(publication_date__lte=datetime.date.today())
	no_of_articles = 0
	article_set = set()
	print("heeloo %s" %start_article_id)
	index = int(start_article_id)
	lenFinal = int(Article.objects.filter(publication_date__lte=datetime.date.today()).order_by('id').last().id)
	print("eeeoo %d" %lenFinal)
	while(no_of_articles<4 and index<lenFinal):
		try:
			article = Article.objects.get(id=start_article_id)
			print ("yes %s" %article)
			if not(alreadyPublishedArticles.filter(id=index).exists()):
				article = None
			if(article!=None and article.hero_image!=None):
				article_set.add(article)
				no_of_articles += 1
		except Article.DoesNotExist:
			article=None
			print ("no")
		index += 1
		start_article_id = str(index)
	return render(request,'Articles/articleSetTemplate.html',{'article_set':article_set})
