from .models import Product
from rest_framework.serializers import ModelSerializer



class ProductSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ("name", "category", "quantity","price","image")

