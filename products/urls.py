from django.urls import path

from . import views


app_name = "products"

urlpatterns = [
    path("", views.IndexListView.as_view(), name="index"),
    path('categories/', views.CategoryView.as_view(), name='category'),
    path("products/", views.ProductList.as_view(), name="products"),
    path("subcategorie/", views.SubCategoryView.as_view(), name="subcategory"),
]
