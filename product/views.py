from unicodedata import category
from django.shortcuts import render
from django.core.paginator import Paginator
from.models import Product, ProductImages, Category
from django.db.models import Count

#Create your views here.


def productlist(request,category_slug=None):
    category = None 
    productlist = Product.objects.all()
    categorylist = Category.objects.annotate(total_products=Count('product'))
    
    if category_slug :
        category = Category.objects.all()
        productlist = productlist.filter(category=category)
    template = 'Product/product_list.html'

    
    
    paginator = Paginator(productlist, 2) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    productlist = paginator.get_page(page_number)
    

   
    context = {'product_list' : productlist, 'category_list' : categorylist}
    return render(request, template, {'product_list' : productlist}, context)

def productdetail(request, product_slug):
    productdetail = Product.objects.get(slug=product_slug)
    productimages = ProductImages.objects.filter(product=productdetail)
    template = 'Product/product_detail.html'
    context = {'product_deatail' : productdetail , 'product_images' : productimages} 
    return render(request, template, context)