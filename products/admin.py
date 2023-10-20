from django.contrib import admin
from . models import *


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("category",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name",)