from django.db import models
from datetime import datetime
# Create your models here.
class Event(models.Model):
	title = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	venue = models.CharField(max_length=200)
	description =models.TextField(blank=True)
	ticketprice = models.TextField()
	phone = models.CharField(max_length=20)
	photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
	photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
	photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
	photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
	is_published = models.BooleanField(default=True)
	list_date = models.DateTimeField(default=datetime.now, blank=True)
	def __str__(self):
		return self.title
class UserEvent(models.Model):
	title = models.CharField(max_length=200,default="")
	address = models.CharField(max_length=200,default="")
	venue = models.CharField(max_length=200,default="")
	description =models.TextField(blank=True,default="")
	contact =models.TextField(blank=True,default="")
	
	def __str__(self):
		return self.title