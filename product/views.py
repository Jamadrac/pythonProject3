#from django.http import HttpReponse
from django.shortcuts import render
from.models import Product

#Create your views here.


def productlist(request):

    return render(request, product_list.html)

def productdetails(request, id):
    print (id)
