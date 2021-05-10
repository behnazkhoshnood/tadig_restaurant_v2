from django.shortcuts import render
from django.db import models

from products.models import Product
from products.views import product_detail


def index(request):
    """ A view to return the index page """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)
