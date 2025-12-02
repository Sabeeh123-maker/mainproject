from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from shop.models import Category, Product


class Userform(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','first_name','last_name']
class Loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image','category','stock']

class AddStockForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['stock']