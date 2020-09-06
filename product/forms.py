from django import forms
from .models import Product,Category
from mptt.forms import MoveNodeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class ProductForm(forms.ModelForm):
      class Meta:
            model = Product
            fields = ['name','category','price','image']
     

class CategoryForm(MoveNodeForm):
      class Meta:
            model = Category
            fields = ['name','parent','description','image']