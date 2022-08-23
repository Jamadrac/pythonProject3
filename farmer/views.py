from django.shortcuts import render
#from product.models import Product , Category
# Create your views here.

#@login_required
def dashboard(request):
    
    #products = Product.objects.all()
    #all_category = Category.objects.all() 
 #   current_user = request.User


    template = 'dashboard.html'
    #context = { 'all_category' : all_category , 'products' : products}

    return render(request , template ,)