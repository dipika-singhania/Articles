from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Article,Category
# Create your views here.
def index(request):
	alreadyPublishedArticles = Article.objects.filter(publication_date__lte=datetime.date.today())
	if len(alreadyPublishedArticles)!=0:
		return render(request, 'Articles/index.html', {'alreadyPublishedArticles': alreadyPublishedArticles[:4]})
	else:
		return HttpResponse(":-\( kattish babay")
	
def detail(request, article_id):
	return HttpResponse("hello dipika nice job , keep going %" , article_id)