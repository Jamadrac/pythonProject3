from itertools import product
from django.contrib import admin

# Register your models here.
from .models import Product, Category, OrderItem, ProductImages

admin.site.register(Product)
admin.site.register(Category)
#admin.site.register(Brand)
admin.site.register(ProductImages)
admin.site.register(OrderItem)