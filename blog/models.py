from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100,null=False)
    slug = models.SlugField(null=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

    def  get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
    
    
    
