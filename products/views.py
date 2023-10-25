from django.views.generic import ListView
from django.views.generic import TemplateView

from .models import Category
from .models import Product
from .models import SubCategory
from .models import TopCategory

class IndexListView(ListView):
    model = Product
    template_name = "products/index.html"
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['subcategories'] = SubCategory.objects.all()
        context['subcategories'] = SubCategory.objects.all()
        context['top_categories'] =  TopCategory.objects.all()
        return context


class CategoryView(TemplateView):
    template_name = "products/categorie_list.html"


class SubCategoryView(TemplateView):
    template_name = "products/subcategorie_list.html"


class ProductList(ListView):
    model = Product
    template_name = "products/products_list.html"
