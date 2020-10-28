from django.db import models

class Widget(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField(max_length=200)
    features = models.TextField(max_length=200)
    mainPicBig = models.CharField(max_length=100)
    mainPicSmall = models.CharField(max_length=100)
    detailPicBig = models.CharField(max_length=100)
    detailPicSmall = models.CharField(max_length=100)
    quantity = models.IntegerField()