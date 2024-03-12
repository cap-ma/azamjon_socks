from django.db import models

class Banners(models.Model):
    file=models.ImageField(upload_to='media/banners')

class Catalog(models.Model):
    file=models.ImageField(upload_to='media/catalog')

class Product(models.Model):
    title=models.CharField(max_length=128)
    color=models.CharField(max_length=128)
    file=models.ImageField(upload_to='media/products')

class Faq(models.Model):
    question=models.TextField()
    answer=models.TextField()


