from django.urls import path
from . import views
from django.views.generic import ListView


app_name = "products"

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("category/", views.Category.as_view(), name="category"),
    path("products/", views.Product.as_view(), name="products"),
    path("subcategorie/", views.SubCategory.as_view(), name="subcategory"),

]
