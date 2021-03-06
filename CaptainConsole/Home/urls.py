from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home-index"),
    path('<int:id>', views.get_product_by_id, name="home_Product_details"),
    path('add_to_cart/<int:id>', views.add_to_cart, name="add-to-cart")
]
