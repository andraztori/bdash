from django.db import models

# Create your models here.

class Source(models.Model):
	title = models.CharField(max_length=200)
	url = models.URLField(verify_exists=True)
	pubDate = models.DateField(auto_now_add=True)
	chgDate = models.DateField(auto_now=True)

class Infographic(models.Model):
	title = models.CharField(max_length=200)
	source = models.ForeignKey(Source)
	url = models.URLField(verify_exists=True)
	text = models.TextField()
	pubDate = models.DateField(auto_now_add=True)
	chgDate = models.DateField(auto_now=True)	

# class Category(Models.model)

# class Link(Model.model)