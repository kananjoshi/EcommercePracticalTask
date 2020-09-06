from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, JsonResponse
from .models import Product, Category, CartItem, MyCart
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProductForm,CategoryForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import NewUserForm
import logging
import json

def login(request):
      form = NewUserForm(request.POST)
      if form.is_valid():
            form.save()
            form = NewUserForm()
      else:
            print (form.errors) 
      context = {
            'form':form
      }
      return render(request,'product/register.html',context)


def index(request):
      try:

            if request.user.is_authenticated:
                  product_list = Product.objects.all()
                  context = {
                        'products' : product_list 
                  }
                  return render(request,'product/index.html',context)
            else:
                  form = NewUserForm(request.POST)
                  if form.is_valid():
                        form.save()
                        form = NewUserForm()
                  else:
                        print (form.errors) 
                  context = {
                        'form':form
                  }
                  return render(request,'product/register.html',context)
      except ObjectDoesNotExist:
            return render(request,'product/404.html',context)


def detail_view(request, id):
      product = get_object_or_404(Product, pk=id)
      context = {
            'product' : product 
      }
      return render(request,'product/product_detail.html',context)

@login_required
def add_product(request):
      if request.user.is_authenticated and request.user.is_superuser: 
            form = ProductForm(request.POST , request.FILES or None)
            if form.is_valid():
                  product = form.save(commit = False)
                  product.added_by = request.user
                  product.save()
                  form = ProductForm()
            context = {
                  'form':form
            }
            return render(request,'product/add_product.html',context)
      else:
            return HttpResponse('<center> Only Admin Have rights to add the products </center>')



def cart_add(request, id):
      if request.method == 'GET':
            # import pdb;pdb.set_trace()
            mycart, created = MyCart.objects.get_or_create(user = request.user)
            product_qty = request.GET['quantity']
            product = get_object_or_404(Product, pk=id)
            cart_item_product = CartItem.objects.filter(product = product)
            if cart_item_product:
                  cart_item_product.delete()
                  cart_item = CartItem.objects.get_or_create(product = product,
                        quantity = product_qty,
                        price = product.price,
                        cart = mycart)
            else:
                  cart_item = CartItem.objects.get_or_create(product = product,
                        quantity = product_qty,
                        price = product.price,
                        cart = mycart)

            context = {
                  'cart':mycart,
                  'cart_item':cart_item
            }
      return JsonResponse({'result': 'Success'})


def show_cart(request):
      if request.user.is_authenticated:
            user = request.user
            cartdata =  get_object_or_404(MyCart,user=user)
            cart_items = cartdata.cart_items.all()
            # CartItem.objects.filter(cart=cartdata).aggregate(Sum('quantity'))
            context = {
                  "cartdata" : cart_items
            }
            
            return render(request,'product/show_cart.html',context)
      else:
            return render(request,'product/404.html',context)

      

def place_order(request):
      import pdb ; pdb.set_trace()
      if request.user.is_authenticated:
            user = request.user
            cartdata =  get_object_or_404(MyCart,user=user)
            if cartdata :
                  myoder, created  = Order.objects.get_or_create(user = request.user,address="ahmedabad")
                  cartdata.delete()

            


