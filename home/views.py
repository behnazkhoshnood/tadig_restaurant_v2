from django.shortcuts import render
from products.models import Product, Review


def index(request):
    """ A view to return the index page """

    products = Product.objects.all()
    reviews = Review.objects.all()

    context = {
        'products': products,
        'reviews': reviews,
    }

    return render(request, 'home/index.html', context)
