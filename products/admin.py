from django.contrib import admin

from .models import Category
from .models import Product
from .models import ProductImage
from .models import SubCategory
from .models import TopCategory



@admin.register(TopCategory)
class TopCategoryAdmin(admin.ModelAdmin):
    list_display = ("top_category",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("category",)


class ProductInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    list_display = ("name",)
    exclude = ["slug"]
