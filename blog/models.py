from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.EmailField()
    created_date=models.DateField(auto_now_add=True)
class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    blog_title=models.CharField(max_length=100)
    blog_description=models.TextField()
    posted_date=models.DateField(auto_now_add=True)
class comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    Comment=models.CharField(max_length=50)
    comment_date=models.DateTimeField(auto_now_add=True)
