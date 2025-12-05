from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from shop.models import Product
from cart.models import Cart
from cart.forms import OrderForm
import razorpay



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
        form = OrderForm()
        context = {'form':form}
        return render(request, 'checkout.html', context)
    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            o=form.save(commit=False)
            u=request.user
            o.user=u
            c=Cart.objects.filter(user=u)
            t=0
            for i in c:
                t+=i.subtotal()
            print(t)
            o.amount=t
            o.save()
            if(o.payment_method=='online'):
                #1. create a razorpay connection using keys
                client = razorpay.Client(auth=('rzp_test_Rn853YhSiRl2l7','UpKFAcdCLWN1ph277XjeDNcH'))
                #2. creates a new order in razorpay
                response_payment=client.order.create({'amount':(o.amount)*100,'currency':'INR'})
                print(response_payment)
                id=response_payment['id']
                o.order_id=id
                o.save()
                context = {'payment':response_payment}
            else:
                pass
            return render(request, 'payment.html', context)
#csrf excempt-to ignore csrf verification:
@method_decorator(csrf_exempt,name='dispatch')
class Paymentsuccess(View):
    def post(self, request):
        print(request.user.username)
        print(request.POST)
        return render(request, 'payment_success.html')