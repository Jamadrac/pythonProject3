from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name ='product'
urlpatterns = [
    path("" ,views.productlist , name="product_list"),
    path("<slug:category_slug>" ,views.productlist , name="product_list_category"),
    path("<slug:product_slug>" ,views.productdetail , name="product_detail")
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)