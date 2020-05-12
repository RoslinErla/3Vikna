from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name="cart-index"),
    path('add_to_cart/<int:id>', views.add_to_cart, name="add-to-cart"),
    path('checkout', views.checkout, name="checkout"),
    path('read_only', views.read_only_review, name="read-only")
]
