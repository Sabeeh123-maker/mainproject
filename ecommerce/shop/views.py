from django.shortcuts import render,redirect
from django.views import View
from shop.models import Category,Product
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate
from shop.forms import Userform,Loginform,AddCategoryForm,AddProductForm,AddStockForm



# Create your views here.
class CategoryView(View):
    def get(self, request):
        c=Category.objects.all()
        context = {'categories': c}
        return render(request, "category.html",context)

class ProductView(View):
    def get(self, request,i):
        c=Category.objects.get(id=i)
        context = {'category': c}
        return render(request, "product.html",context)

class ProductDetailView(View):
    def get(self, request,i):
        c=Product.objects.get(id=i)
        context = {'product':c}
        return render(request, "product_detail.html",context)

class Registerview(View):
    def get(self, request):
        form_instance = Userform()
        context = {'form2': form_instance}
        return render(request,'register.html',context)
    def post(self, request):
        form_instance = Userform(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)
            form_instance.save()
            return redirect('shop:login')

class Loginview(View):
    def get(self, request):
        form_instance = Loginform()
        context = {'form3': form_instance}
        return render(request,'login.html',context)
    def post(self, request):
        form_instance = Loginform(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data #fetches data after validation
            u=data['username']#retrieves username from cleaned data
            p=data['password']#retrieves username from cleaned data
            user=authenticate(username=u,password=p)#calls authenticate to verify if user exists
                                                    #if user exists then it returns to the user object
                                                    #else none
            if user:#if user exists
                login(request,user)  #add the user into current session
                return redirect('category')
            else: #if not exists
                messages.error(request, "Invalid Username or Password!")
                return redirect('shop:login')

class Logoutview(View):
    def get(self, request):
        logout(request)
        return redirect('shop:login')

class AddProduct(View):
    def get(self, request):
        form_instance = AddProductForm()
        context = {'form': form_instance}
        return render(request,'addproduct.html',context)
    def post(self, request):
        form_instance = AddProductForm(request.POST,request.FILES)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)
            form_instance.save()
            return redirect('shop:addproduct')

class AddCategory(View):
    def get(self, request):
        form_instance = AddCategoryForm()
        context = {'form': form_instance}
        return render(request,'addcategory.html',context)
    def post(self, request):
        form_instance = AddCategoryForm(request.POST,request.FILES)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)
            form_instance.save()
            return redirect('shop:addcategory')

class AddStock(View):
    def get(self, request,i):
        p=Product.objects.get(id=i)
        form_instance = AddStockForm(instance=p)
        context = {'form': form_instance}
        return render(request,'addstock.html',context)
    def post(self, request,i):
        p=Product.objects.get(id=i)
        form_instance = AddStockForm(request.POST,instance=p)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('shop:productdetail',i)

