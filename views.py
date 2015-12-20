from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.core.paginator import Paginator
from .models import Article,Category
# Create your views here.
def index(request):
	alreadyPublishedArticles = Article.objects.filter(publication_date__lte=datetime.date.today())
	page_size = 4
	if len(alreadyPublishedArticles)!=0:
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
		return render(request, 'Articles/index.html', 
		{'alreadyPublishedArticles':alreadyPublishedArticles , 'articlePerPage': articlePerPage}
		)
	else:
		return HttpResponse(":-\( No Articles at all ")
	
def detail(request, article_id):
	return HttpResponse("hello dipika nice job , keep going %" , article_id)