from django.contrib.auth.models import User, auth
from django.db import models
import datetime

"""
This model is used to categorize the grocery items
based on their and description 
"""
class Category(models.Model):
    description = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name


"""
This model is used to uniquely identify a product
with its name, id etc. It saves the info about the 
product  
"""
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.ImageField(upload_to='Images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    @staticmethod
    def fetch_products(id_list):
        return Product.objects.filter(id__in=id_list)

    @staticmethod
    def fetch_products_by_category(cat_id):
        if cat_id:
            return Product.objects.filter(category=cat_id)
        else:
            return Product.objects.all()

"""
This model is used to save the order details for any purchase 
done by the customer
"""
class Order(models.Model):
    address = models.CharField(max_length=250, default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13, default='')
    date = models.DateField(default=datetime.datetime.today)
    quantity = models.IntegerField(default=1)
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def confirm_order(self):
        self.save()


