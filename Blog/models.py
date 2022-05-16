from email.policy import default
from pyexpat import model
from time import timezone
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class User(AbstractUser):
    contactno=models.CharField(max_length=10,unique=True,null=True)
    twitter_api_key=models.CharField(max_length=255,null=True)
    twitter_api_key_secret=models.CharField(max_length=255,null=True)
    twitter_access_token=models.CharField(max_length=255,null=True)
    twitter_access_token_secret=models.CharField(max_length=255,null=True)
    insta_username=models.CharField(max_length=255,null=True)
    insta_password=models.CharField(max_length=255,null=True)
    facebook_access_token=models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.username
    
class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    content=models.TextField()
    image=models.ImageField()
    is_twitter=models.BooleanField('Twitter',default=False)
    is_facebook=models.BooleanField('Facebook',default=False)
    is_instagram=models.BooleanField('Instagram',default=False)
    created_date=models.DateTimeField(default=timezone.now)
    
    @property
    def imageurl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 

    class Meta:
        ordering=('created_date',)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('userhome')


