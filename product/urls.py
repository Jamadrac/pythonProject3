from django.urls import path
from . import views


urlpatterns = [
    path("" ,views.productlist , name="product_list"),
    path("<int:id>",views.productdetails , name="product_detail")
]