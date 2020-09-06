from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext as _
from datetime import datetime
from django.contrib.auth.models import User


class Category(MPTTModel):
      class Meta:
            verbose_name = _("Product Category")
            verbose_name_plural = _("Product Categories")

      class MPTTMeta:
            order_insertion_by = ['name']

      parent = TreeForeignKey('self', on_delete=models.CASCADE, 
                              null=True, blank=True,  
                              related_name='children')
      name = models.CharField(max_length=30)
      description = models.CharField(max_length=255)
      image = models.ImageField(upload_to='images/',blank=True, null=True)
      created_at = models.DateTimeField(auto_now=True)
      added_by = models.ForeignKey(User,
        null=True, blank=True, on_delete=models.SET_NULL)

      def __str__(self):
            return "{}".format(self.name)

class Product(models.Model):
      class Meta:
            verbose_name = _("Product")
            verbose_name_plural = _("Products")

      name = models.CharField(max_length=30)
      price = models.DecimalField(max_digits=10, decimal_places=2)
      category = models.ForeignKey(Category,on_delete=models.CASCADE)
      quantity = models.PositiveIntegerField( blank=False, 
                                                null=False, default = 1)
      image = models.ImageField(upload_to='images/',blank=True, null=True)
      created_at = models.DateTimeField(auto_now=True)
      added_by = models.ForeignKey(User,
        null=True, blank=True, on_delete=models.SET_NULL)

      def __str__(self):
            return "[PRODUCT] {}".format(self.name)

class MyCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    

class CartItem(models.Model):
      product = models.OneToOneField(Product, on_delete=models.CASCADE)
      quantity = models.IntegerField(default=1)
      price = models.FloatField(blank=True)
      cart = models.ForeignKey(MyCart, on_delete=models.CASCADE,related_name='cart_items')

      def __str__(self):
            return "Product {}".format(self.product.name)

class Order(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      created_at = models.DateTimeField(default=datetime.now)
      address = models.CharField(max_length=50)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='item', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.PositiveIntegerField(default=1)

      
