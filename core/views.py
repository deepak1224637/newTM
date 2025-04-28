from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product
from orders.models import Order
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Home page function
def home(request):
    products = Product.objects.all()  # Fetch all products for homepage
    return render(request, 'core/home.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'core/product_list.html', {'products': products})

# Product detail function
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'core/product_detail.html', {'product': product})

def buy_now(request, pk):
    product = get_object_or_404(Product, pk=pk)
    Order.objects.create(user=request.user, product=product, quantity=1)

     # Create the order here
    order = Order.objects.create(user=request.user, product_name=product.name, quantity=1, )  # Assuming 1 item is being bought

    return redirect('dashboard')
