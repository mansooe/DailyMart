

from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    CategoryName=models.CharField(max_length=200,null=True,blank=False)
    CategoryImg=models.ImageField(upload_to='media',null=True,blank=False)
class ProductDb(models.Model):
    productname=models.CharField(max_length=200,null=True,blank=False)
    productimg=models.ImageField(upload_to='media/ProductImages',null=True,blank=False)
    productcategory=models.CharField(max_length=200,null=True,blank=False)
    productprice=models.IntegerField()
