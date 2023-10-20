from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class SubCategory(models.Model):
    name=models.CharField(max_length=100)
    category = models.ForeignKey(Category, verbose_name=("category"), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category=models.ForeignKey(Category, verbose_name=("Category"), on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="products")
    price = models.FloatField()

    def _str_(self):
        return self.name


