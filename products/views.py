from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import TemplateView
from .models import SubCategory, Product, Category


class IndexListView(ListView):
    model = Product
    template_name = "products/index.html"
    context_object_name = 'products' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['subcategories'] = SubCategory.objects.all()
        return context


class CategoryView(TemplateView):
    template_name = "products/categorie_list.html"


class SubCategoryView(TemplateView):
    template_name = "products/subcategorie_list.html"  


class ProductList(ListView):
    model = Product
    template_name = "products/products_list.html"      
