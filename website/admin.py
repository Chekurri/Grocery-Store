"""
This python file handles the admin related
works
"""
from django.contrib import admin
from .models import Product,  Order, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'quantity', 'price', 'address', 'phone', 'date', 'status')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category, CategoryAdmin)
