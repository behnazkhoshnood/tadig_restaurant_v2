from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('products/<product_id>', views.product_detail, name='product_detail'),
]
