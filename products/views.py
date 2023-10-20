from django.shortcuts import render
from django.views.generic import ListView
from . models import *

# Create your views here.
class Index(ListView):
    model = Category
    template_name = "web/index.html"


class Category(ListView):
    model = Category
    template_name = "products/categorie_list.html"

class SubCategory(ListView):
    model = SubCategory
    template_name = "products/subcategorie_list.html"  

class Product(ListView):
    model = Product
    template_name = "products/products_list.html"      
