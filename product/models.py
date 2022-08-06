from distutils.command.upload import upload
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    Category_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/', blank=True, null=True)


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.Category_name


class type(models.Model):
    Brand_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.Brand_name


class Product(models.Model):
    CONDITION_TYPE = (
        ("fresh", "fresh"),
        ("dry", "dry")
    )
    CLASS_TYPE = (
        ("vegetable", "vegetable"),
        ("frut", "frut"),
        ("meat","meat")
    )
    # all products imformations of luwi the idiots
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=48)
    city_name = models.CharField(max_length=20)
    description = models.TextField(max_length=48)
    condition = models.CharField(max_length=100, choices=CONDITION_TYPE)
    food_type = models.CharField(max_length=100, choices=CLASS_TYPE)
    image = models.ImageField(upload_to='main_product/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    #brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=3)
    created = models.DateTimeField(default=timezone.now)

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Product, self).save (*args, **kwargs)       

    def __str__(self):
        return self.name

class ProductImages(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/', blank=True, null=True)

    def __str__(self):
        return self.product.name
    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product imeges'

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()
