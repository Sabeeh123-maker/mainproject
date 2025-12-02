from django.shortcuts import render, redirect
from django.views import View
from shop.models import Product
from cart.models import Cart


# Create your views here.
class AddCartView(View):
    def get(self, request,i):
        p=Product.objects.get(id=i)
        u=request.user
        try:
            c=Cart.objects.get(user=u,product=p)
            c.quantity+=1
            c.save()
        except:
            c = Cart.objects.create(user=u,product=p,quantity=1)
            c.save()
        return redirect('cart:cartview')

class CartView(View):
    def get(self, request):
        u=request.user
        c=Cart.objects.filter(user=u)
        sum=0
        for i in c:
            sum = sum + i.subtotal()
        print(c)
        context = {'cart':c,'total':sum}
        return render(request, 'cart.html',context)
class DecrementCartView(View):
    def get(self, request,i):
        c = Cart.objects.get(id=i)
        if(c.quantity>1):
            c.quantity -= 1
            c.save()
        else:
            c.delete()

        return redirect('cart:cartview')
class DeleteProduct(View):
    def get(self, request,i):
        c=Cart.objects.get(id=i)
        c.delete()
        return redirect('cart:cartview')

class CheckoutView(View):
    def get(self, request):
        return render(request, 'checkout.html')