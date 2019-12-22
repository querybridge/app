from django.db import models
from django.utils.text import slugify
from .utils import COLOR_CHOICES, FINISH_CHOICES


# Create your models here.

class Product(models.Model):
    brand = models.CharField(max_length=255)
    series = models.CharField(max_length=255)
    style = models.CharField(max_length=255, default="Style")
    description = models.TextField(default="Description")

class Attribute(Product):
    attribute_sku = models.OneToOneField(Product, on_delete=models.CASCADE, parent_link=True)
    diameter = models.IntegerField(default=0)
    color = models.CharField(max_length=255, choices=COLOR_CHOICES)
    finish = models.CharField(max_length=255, choices=FINISH_CHOICES)

class Location(Product):
    location_sku = models.OneToOneField(Product, on_delete=models.CASCADE, parent_link=True)
    Austell = models.IntegerField(default=0)
    Alpharetta = models.IntegerField(default=0)
    Buckhead = models.IntegerField(default=0)
    Marietta = models.IntegerField(default=0)
    Central = models.IntegerField(default=0)

class Wheel(Attribute, Location):
    sku = models.SlugField(default='1')

    def save(self, *args, **kwargs):
        self.sku = slugify([self.brand, self.series, self.style])
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.sku
