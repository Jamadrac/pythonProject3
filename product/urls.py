from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name ='product'
urlpatterns = [
    path("products/" ,views.productlist , name="product_list"),
    path("<slug:category_slug>" ,views.productlist , name="product_list_category"),
    path("<slug:product_slug>" ,views.productdetail , name="product_detail"),
    
    # ANDREW
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include("users.urls"))
]