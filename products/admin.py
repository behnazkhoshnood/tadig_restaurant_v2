from django.contrib import admin
from .models import Product, Category, Review, Wishlist

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'comment',
        'rating',
    )

    readonly_fields = (
        'product',
        'user',
        'comment',
        'rating',
    )


class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'wished_product', 'added_date']
    readonly_fields = ('user', 'wished_product', 'added_date')
    ordering = ('added_date',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review)
admin.site.register(Wishlist, WishlistAdmin)
