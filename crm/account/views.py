from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    template_name='account/dashboard.html'
    return render(request, template_name)


def products(request):
    template_name='account/products.html'
    return render(request, template_name)


def customer(request):
    template_name='account/customer.html'
    return render(request, template_name)
