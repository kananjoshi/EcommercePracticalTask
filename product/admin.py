from django.contrib import admin
from .models import Product,Category,MyCart,CartItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','price','quantity']
    list_search  = ['name','category','price','quantity']

    def save_model(self, request, obj, form, change):
        
        obj.added_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Product,ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)

    list_display = ['name','parent']
    list_search  = ['name']
    exclude = ['added_by']

admin.site.register(Category,CategoryAdmin)

admin.site.register(MyCart)
admin.site.register(CartItem)