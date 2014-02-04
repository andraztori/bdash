from django.db import models
from feedjack.models import Post

# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=200)
	slug = models.CharField(max_length=200)
	description = models.TextField()
	pubDate = models.DateField(auto_now_add=True)
	chgDate = models.DateField(auto_now=True)
	
	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
	    return "/%s/" % self.slug
    
class Source(models.Model):
	title = models.CharField(max_length=200)
	url = models.URLField(verify_exists=True)
	pubDate = models.DateField(auto_now_add=True)
	chgDate = models.DateField(auto_now=True)

	def __unicode__(self):
		return self.title

class Infographic(models.Model):
	title = models.CharField(max_length=200)
	source = models.OneToOneField(Post)
	category = models.ForeignKey(Category)
	url = models.URLField(verify_exists=True)
	text = models.TextField()
	imageurl = models.URLField()
	pubDate = models.DateField(auto_now_add=True)
	chgDate = models.DateField(auto_now=True)	

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
	    return self.url
