from django.shortcuts import render
from products.views import product_detail

from products.models import Product

def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')
