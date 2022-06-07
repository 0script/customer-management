from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import (
    Product,
    Order,
    Customer
    )

from .forms import OrderForm

# Create your views here.

def home(request):
    'View for the dashboard'
    template_name='account/dashboard.html'

    customers=Customer.objects.all()
    orders=Order.objects.all()
    delivered=Order.objects.filter(status='Delivered').count()
    pending=Order.objects.filter(status='Pending').count()

    customer_count=customers.count()
    order_count=orders.count()
    

    context={
        
        'customers':customers,
        'customer_count':customer_count,
        'orders':orders,
        'order_count':order_count,
        'pending':pending,
        'delivered':delivered,
        
    }
    return render(request, template_name,context=context)


def products(request):
    'View for the product page'
    template_name='account/products.html'

    products=Product.objects.all()
    context={
        'products':products,
    }
    return render(request, template_name,context=context)


def customer(request,pk):
    template_name='account/customer.html'

    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    order_count=orders.count()

    context={
        'customer':customer,
        'orders':orders,
        'order_count':order_count,
    }

    return render(request, template_name,context=context)

def create_order(request):
    template_name='account/order-form.html'

    form=OrderForm()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={
        'form':form,
    }

    return render(request, template_name,context=context)