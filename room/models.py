from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify



class Room(models.Model):
	owner = models.ForeignKey(User,on_delete = models.SET_NULL,null=True)
	title = models.CharField(max_length=50)
	description = models.TextField()
	created = models.DateField(auto_now_add=True, null=True,blank=True)
	modify = models.DateField(auto_now=True)
	participants = models.ManyToManyField(User,related_name='participants', blank=True)
	category = models.ForeignKey('Category', on_delete = models.SET_NULL, null=True)
	slug = models.SlugField(blank=True,null=True)

	def save(self,*args,**kwargs):
		self.slug = slugify(self.title)
		super(Room,self).save(*args,**kwargs)



	class Meta:
		ordering = ['-modify']

	def __str__(self):
		return self.title

class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Comment(models.Model):
	user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
	body = models.CharField(max_length=150)
	room = models.ForeignKey(Room,on_delete=models.SET_NULL,null=True)

	def __str__(self):
		return str(self.user)