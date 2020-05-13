from django.db import models
from django.contrib.auth.models import User
from AllProducts.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Checkout(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Full_name = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Postal_code = models.FloatField()
    Name_of_cardholder = models.CharField(max_length=999)
    Card_number = models.CharField(max_length=19)
    Expiration_date = models.DateField()
    CVC = models.CharField(max_length=3)
