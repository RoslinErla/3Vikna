from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name="cart-index"),
    path('add_to_cart/<int:id>', views.add_to_cart, name="add-to-cart"),
    path('checkout', views.checkout, name="checkout"),
    path('read_only', views.read_only_review, name="read-only"),
    path('success', views.success, name="success"),
    path('remove/<int:id>', views.remove_product, name="remove"),
    path('', views.cart, name="empty-cart")
]
