from django.db import models
from profiles.models import UserProfile


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254, null=True, blank=True
        )
    slug= models.SlugField(max_length=225)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', related_name='products', null=True, blank=True, on_delete=models.SET_NULL
        )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    slug= models.SlugField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(
        Product, related_name='reviews', on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    user_name = models.ForeignKey(
        UserProfile, related_name='reviews', on_delete=models.CASCADE
    )
    comment = models.TextField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True)
