from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse

from store.models import Product, Cart, Order

# Create your views here.
def home(response):
    return HttpResponse('Hello World')
def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', context={'pdt':products})

def product_details(request, slug):
    #product = Product.objects.get(slug=lug) this is same as below code
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', {'products':product})

def add_to_cart(request, slug):
    #here to get the user and store him inside user variable
    user = request.user
    product = get_object_or_404(Product, slug=slug) # get the product and pass in slug. and if the product does not exist an error 404
    cart, _ =Cart.objects.get_or_create(user=user)  # if product exist we get the user cart, if the cart doe not exist, then it's created and if it exist then it's gotten and assign to the variable cart
    order, created = Order.objects.get_or_create(user=user,
                                                 product=product)  # checck if user has pass previous order which correspond to product we want to add
    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse("products", kwargs={"slug": slug}))

def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, "store/cart.html", context={"orders":cart.orders.all()})

def delete_cart(request):
    if cart := request.user.cart:
        cart.orders.all().delete()
        cart.delete()
    return redirect('index')


"""
in older version of python, to delete we could do the following

def delete_cart(request):
    cart = request.user.cart
    if cart:                    or town lines in one    (if cart := request.user.cart:)                 
        cart.orders.all().delete()
        cart.delete()
    return redirect('index')
"""