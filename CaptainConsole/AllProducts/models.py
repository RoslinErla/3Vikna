from django.db import models

# Create your models here.
class AllProducts(models.Model)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    type = models.CharField(max_lenght=255)
    manufacturer = models.ForeignKey()  # map to manufacturer
    price = models.FloatField()
    on_sale = models.BooleanField()


class ProductImage(models.Model):
    image = models.CharField(max_length=999)
    product = models.ForeignKey(AllProducts, on_delete=models.CASCADE)
