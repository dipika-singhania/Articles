#!/usr/bin/python
import random
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#!/usr/bin/python
import random
from .models import Article,Category
from django.template import RequestContext, loader

# Create your views here.
def index(request):
	alreadyPublishedArticles = Article.objects.filter(publication_date__lte=datetime.datetime.today()).order_by('publication_date')
	return render(request, 'Articles/ArticleList.html', {'alreadyPublishedArticles':alreadyPublishedArticles})
	
def detail(request, article_id):
	alreadyPublishedArticles = Article.objects.filter(publication_date__lte=datetime.datetime.today()).order_by('publication_date')
	try:
		article_detail = Article.objects.get(id=article_id)
	except Article.DoesNotExist:
		article_detail = None;
	return render(request, 'Articles/ArticleDetail.html' , {'article_detail':article_detail})
	
def random_generator(request):
	alreadyPublishedArticles = list(Article.objects.filter(publication_date__lte=datetime.datetime.today()))
	lenFinal = len(alreadyPublishedArticles)
	lenStart = 0
	article_random = None
	iter = 0
	while(article_random==None or iter<100):
		index = random.randrange(lenStart, lenFinal)
		try:
			article_random = alreadyPublishedArticles[index]
			if(not(article_random.hero_image)):
				article_random = None
		except Article.DoesNotExist:
			article_random = None
		iter += 1
	return render(request, 'Articles/detailSnippet.html',{'article_random': article_random})

def prevArticleSet(request):
	alreadyPublishedArticles = Article.objects.filter(publication_date__lte=datetime.datetime.today())
	page_size = 4
	paginator = Paginator(alreadyPublishedArticles, page_size)
	if( 'page_number' in request.session ):
		current_page_num = request.session['page_number']
	else:
		current_page_num = 1
		
	current_page = paginator.page(current_page_num)
	
	if( current_page.has_previous()):
		previous_page_num = int(current_page.previous_page_number())
	else:
		previous_page_num = current_page_num
	request.session['page_number'] = previous_page_num
	try:
	   article_set = paginator.page(previous_page_num)
	except PageNotAnInteger:
		article_set = paginator.page(1)
	except EmptyPage:
		article_set = paginator.page(paginator.num_pages)
	except:
		article_set = set()
	return render(request,'Articles/articleSetTemplate.html',{'article_set':article_set})
	
def nextArticleSet(request):
	alreadyPublishedArticles = Article.objects.filter(publication_date__lte=datetime.datetime.today())
	page_size = 4
	paginator = Paginator(alreadyPublishedArticles, page_size)
	if( 'page_number' in request.session ):
		current_page_num = int(request.session['page_number'])
	else:
		current_page_num = 1
		
	current_page = paginator.page(current_page_num)
	
	if( current_page.has_next()):
		next_page_num = int(current_page.next_page_number())
	else:
		next_page_num = current_page_num

	request.session['page_number'] = next_page_num
	try:
	   article_set = paginator.page(next_page_num)
	except PageNotAnInteger:
		article_set = paginator.page(1)
	except EmptyPage:
		article_set = paginator.page(paginator.num_pages)
	except:
		article_set = set()
	return render(request,'Articles/articleSetTemplate.html',{'article_set':article_set})

def currArticleSet(request):
	alreadyPublishedArticles = Article.objects.filter(publication_date__lte=datetime.datetime.today())
	page_size = 4
	paginator = Paginator(alreadyPublishedArticles, page_size)
	if( 'page_number' in request.session ):
		current_page_num = int(request.session['page_number'])
	else:
		current_page_num = 1
	current_page = paginator.page(current_page_num)
	request.session['page_number'] = current_page_num
	try:
	   article_set = paginator.page(current_page_num)
	except PageNotAnInteger:
		article_set = paginator.page(1)
	except EmptyPage:
		article_set = paginator.page(paginator.num_pages)
	except:
		article_set = set()
	return render(request,'Articles/articleSetTemplate.html',{'article_set':article_set})
