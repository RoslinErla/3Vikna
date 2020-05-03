from django.db import models

# Create your models here.
class Accessories(models.Model):
    name = models.charfield(max_length=2555)
    description = models.charfield(max_length=999, blank=True)
