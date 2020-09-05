from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.core.exceptions import ObjectDoesNotExist
import logging
# Create your views here.
def index(request):
      try:
            product_list = Product.objects.all()
            context = {
                  'products' : product_list 
            }
            # import pdb ; pdb.set_trace()
            return render(request,'product/index.html',context)
      except ObjectDoesNotExist:
            return render(request,'product/404.html',context)


def detail_view(request, id):
      
      try:
            id =  int(id)
            product = Product.objects.get(pk=id)
            context = {
                  'product' : product 
            }
            return render(request,'product/product_detail.html',context)
      except ObjectDoesNotExist:
            return render(request,'product/404.html',context)
      except ValueError:
            logging.info("Value Error")
            return HttpResponse()
            


      
