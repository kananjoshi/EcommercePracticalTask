from django.db import models

from django.utils.translation import ugettext as _

# Create your models here.
class Product(models.Model):
      class Meta:
            verbose_name = _("Product")
            verbose_name_plural = _("Products")

      name = models.CharField(max_length=30)
      price = models.DecimalField(max_digits=10, decimal_places=2)


      def __str__(self):
            return self.name

