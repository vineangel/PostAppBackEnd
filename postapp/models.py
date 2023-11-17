from django.db import models

# Create your models here.
class PostDetails(models.Model):
    userid=models.CharField(max_length=100,default="")
    title=models.CharField(max_length=100,default="")
    message=models.CharField(max_length=100,default="")

class UserDetails(models.Model):
    userid=models.CharField(max_length=100,default="")
    name=models.CharField(max_length=100,default="")
    email=models.CharField(max_length=100,default="")
    password=models.CharField(max_length=100,default="")
    profile=models.CharField(max_length=100,default="")
