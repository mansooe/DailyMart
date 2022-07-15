
from django.db import models



# Create your models here.
class UserDb(models.Model):
    username=models.CharField(max_length=500,null=True)
    password=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=100,null=True)
class ContactusDb(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    messege=models.CharField(max_length=500,null=True)    

class UserCartDb(models.Model):
    productId=models.CharField(max_length=200)    
