from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	num = models.CharField(max_length=50)
	about = models.TextField(null=True,blank=True)
	slug = models.SlugField(blank=True,null=True)

	def save(self,*args,**kwargs):
		self.slug = slugify(self.user.username)
		super(Profile,self).save(*args,**kwargs)


	def __str__(self):
		return str(self.user)




@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)