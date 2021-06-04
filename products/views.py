from django.shortcuts import (
    render, redirect, reverse,
    get_object_or_404, HttpResponseRedirect)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .forms import ProductForm, ReviewForm
from .models import Product, Category, Review, Wishlist
from profiles.models import UserProfile


# Create your views here.
def all_products(request):
    """ A view to show all products, including sorting and search queries """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    current_user_prdct_id = []
    whishlist_obj = Wishlist.objects.all()
    if request.user.is_authenticated:
        current_user_whishlist = whishlist_obj.filter(user=request.user)
        for itm in current_user_whishlist:
            current_user_prdct_id.append(itm.wished_product.id)

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,
                    "You didn't enter any search criteria!"
                    )
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
            )
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'current_user_prdct_id': current_user_prdct_id,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product__id=product_id)
    current_user_prdct_id = []
    whishlist_obj = Wishlist.objects.all()
    if request.user.is_authenticated:
        current_user_whishlist = whishlist_obj.filter(user=request.user)
        for itm in current_user_whishlist:
            current_user_prdct_id.append(itm.wished_product.id)

    context = {
        'product': product,
        'reviews': reviews,
        'current_user_prdct_id': current_user_prdct_id,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """ A view to add review to a product"""

    product = Product.objects.get(pk=product_id)
    url = request.META.get('HTTP_REFERER')

    if request.method == "POST":
        form_data = {
            "comment": request.POST["comment"],
            "rating": request.POST.get('rating', False)
        }
        form = ReviewForm(form_data)

        if form.is_valid():
            data = form.save(commit=False)
            data.comment = request.POST["comment"]
            data.rating = request.POST.get('rating', False)
            data.user = request.user
            data.product = product
            data.save()
            messages.success(request, 'Your review has been sent!')
            return HttpResponseRedirect(url)
        else:
            messages.error(
                request,
                'Failed to submit review. Please ensure the form is valid.')

    return HttpResponseRedirect(url)


@login_required
def edit_review(request, product_id, review_id):
    """A view to edit product reviews"""

    product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(Review, product=product, pk=review_id)

    if request.user == review.user:
        if request.method == "POST":
            form = ReviewForm(
                request.POST, request, instance=review)
            if form.is_valid():
                data = form.save(commit=False)
                data.save()
                messages.success(request, 'Review updated!')
                return redirect('product_detail', product_id)
            else:
                messages.error(
                    request,
                    'Update review failed. Please ensure the form is valid.')
                return redirect('product_detail', product_id)
        else:
            form = ReviewForm(instance=review)
            return render(request, 'products/editreview.html', {"form": form})
    else:
        return redirect('product_detail', product_id)


@login_required
def delete_review(request, product_id, review_id):
    """A view to delete product review"""

    product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(Review, product=product, pk=review_id)

    if request.user == review.user:
        review.delete()
        messages.success(request, 'Review delete successfully')

    return redirect('product_detail', product_id)


@login_required
def add_to_wishlist(request):
    """
    Handles wishlist post requests:
    checks wishlist model : if the product is already in
    the request.user's  wishlist if so :
    it takes it out, else it adds the product
    """
    url = request.META.get('HTTP_REFERER')
    if request.is_ajax() and request.POST and 'attr_id' in request.POST:
        if request.user.is_authenticated:
            data = Wishlist.objects.filter(
                user_id=request.user.pk,
                wished_product_id=int(request.POST['attr_id'])
            )
            if data.exists():
                data.delete()
            else:
                Wishlist.objects.create(
                    user_id=request.user.pk,
                    wished_product_id=int(request.POST['attr_id'])
                )
    else:
        messages.error(
            request, 'Error adding item to wishlist, please try again.'
        )

    return HttpResponseRedirect(url)


@login_required
def wishlist_view(request):
    """
    A view to display all wishlist items
    belonging to the user in session
    """
    wishlist = {}
    if request.method == "GET":
        if request.user.is_authenticated:
            wishlist = Wishlist.objects.filter(user_id=request.user.pk)
        else:
            messages.error(request, 'kindly login to see your wishlist')
            return redirect('login')
    context = {
        "wishlist": wishlist
    }

    return render(request, 'products/wishlist.html', context)
