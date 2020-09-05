from django.contrib import admin
from .models import Product,Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','price','quantity']
    list_search  = ['name','category','price','quantity']

admin.site.register(Product,ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','parent']
    list_search  = ['name']

admin.site.register(Category,CategoryAdmin)