from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Category(models.Model):
    Category_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/', blank=True, null=True)


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.Category_name


class Brand(models.Model):
    Brand_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.Brand_name


class Product(models.Model):
    CONDITION_TYPE = (
        ("new", "new"),
        ("used", "used")
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # all products imformations of luwi the idiots
    name = models.CharField(max_length=48)
    description = models.TextField(max_length=48)
    condition = models.CharField(max_length=100, choices=CONDITION_TYPE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=3)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class ProductImages(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.product.name
    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product imeges'