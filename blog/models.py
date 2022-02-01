from email.quoprimime import body_check
from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100,null=False)
    slug = models.SlugField(null=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
