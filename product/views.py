from itertools import product
from django.shortcuts import render
from django.core.paginator import Paginator
from.models import Product, ProductImages, Category
from django.db.models import Count, Q
#Create your views here.
from django.views.generic import ListView


def productlist(request,category_slug=None):
    category = None 
    productlist = Product.objects.all()
    categorylist = Category.objects.annotate(total_products=Count('product'))
    
    if category_slug :
        category = Category.objects.get(slug=category_slug)
        productlist = productlist.filter(category=category)

    search_query = request.GET.get('q')
    if search_query:
       productlist = productlist.filter (
         Q(name__icontains = search_query) |
        Q(description__icontains = search_query) |
        Q(food_type__icontains = search_query) |
        Q(category__Category_name__icontains = search_query) 
       )

    paginator = Paginator(productlist,3) # Show 25 contacts per page.
    page = request.GET.get('page',1)
    productlist = paginator.get_page(page)
    template = 'Product/product_list.html'

    context = {'product_list' : productlist, 'category_list' : categorylist, 'category' : category }
    return render(request, template,  context)

    

def productdetail(request, product_slug):
    productdetail = Product.objects.get(slug=product_slug)
    productimages = ProductImages.objects.filter(product=productdetail)
    template = 'Product/product_detail.html'
    context = {'product_deatail' : productdetail , 'product_images' : productimages} 
    return render(request, template, context)