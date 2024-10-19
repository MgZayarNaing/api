from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class  Products(models.Model):
    name = models.CharField(max_length=200)
    image  = models.ImageField(upload_to='products/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='products')
    created_at  = models.DateTimeField(auto_now_add=True)

