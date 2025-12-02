from django.db import models



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    price = models.FloatField()
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)#only one time insert when we add
    updated = models.DateTimeField(auto_now=True)#everytime changes when we update
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='products')
    def __str__(self):
        return self.name
