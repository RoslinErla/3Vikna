from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    price = models.FloatField()
    manufacturer = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

class ProductImage(models.Model):
    image = models.CharField(max_length=999)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
