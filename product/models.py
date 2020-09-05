from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext as _

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



      def __str__(self):
            return self.name

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


      def __str__(self):
            return self.name




      
