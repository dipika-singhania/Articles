from django.db import models

class Category(models.Model):
	category_choice = models.CharField(primary_key=True,max_length=200)
	def __str__(self):
		return self.category_choice
		
class Article(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=40)
	publication_date = models.DateField()
	category_name = models.ForeignKey(Category,on_delete=models.CASCADE)
	hero_image = models.ImageField (upload_to='hero_images/', null=True, blank=True)
	additional_image = models.ImageField (upload_to='addtional_images/', null=True, blank=True)
	article_text = models.TextField()
	def __str__(self):
		return self.title+";"+self.author;