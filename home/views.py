from django.shortcuts import render, get_object_or_404
from django.db import models

from products.models import Product


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def carousel(request, product_id):
    """ A view to show individual product details link to it's carousel image"""

    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
