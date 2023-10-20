from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"


class SubCategory(models.Model):
    name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='subcategory')
    category = models.ForeignKey(Category, verbose_name=("category"), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "SubCategories" 


class Product(models.Model):
    category=models.ForeignKey(SubCategory, verbose_name=("subcategory"), on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    image = models.ImageField(upload_to="products")
    description = HTMLField(null=True, blank=True)
    price = models.FloatField()

    def _str_(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ProductImage(models.Model):
    name = models.ForeignKey(Product, verbose_name=("productimage"), on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productimages')

    def _str_(self):
        return self.name
    
