from django.db import models
from .validators import validate_file_size


class Product(models.Model):
    picture = models.ImageField(upload_to='product_pictures/',
                                max_length=255,
                                validators=[validate_file_size],
                                blank=True)
    title = models.CharField(max_length=48)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=24)
    picture = models.ImageField(upload_to='category_pictures/',
                                max_length=255,
                                validators=[validate_file_size],
                                blank=True)
    background = models.ImageField(upload_to='background/',
                                   max_length=255,
                                   validators=[validate_file_size],
                                   blank=True)

    def __str__(self):
        return self.title
