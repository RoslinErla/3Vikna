from django.db import models
from django.contrib.auth.models import User
from AllProducts.models import Product


class Search(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
