from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="allProducts-index"),
    path('price/', views.index2, name="allProducts-index2"),
    path('price/<int:id>', views.get_product_by_id, name="allProduct_details"),
    path('nintendo/', views.index3, name="allProducts-index3"),
    path('nintendo/<int:id>', views.get_product_by_id, name="allProduct_details"),
    path('atari/', views.index4, name="allProducts-index4"),
    path('atari/<int:id>', views.get_product_by_id, name="allProduct_details"),
    path('sega/', views.index5, name="allProducts-index5"),
    path('sega/<int:id>', views.get_product_by_id, name="allProduct_details"),
    path('playstation/', views.index6, name="allProducts-index6"),
    path('playstation/<int:id>', views.get_product_by_id, name="allProduct_details"),
    path('<int:id>', views.get_product_by_id, name="allProduct_details"),
    path('create_product/', views.create_product, name="create_product"),
    path('delete_product/<int:id>', views.delete_product, name="delete_product"),
    path('update_product/<int:id>', views.update_product, name="update_product"),
    path('atari/price/', views.index7, name='allproducts-atari-sorted-price'),
    path('atari/price/<int:id>', views.get_product_by_id, name="allProduct_details"),
    path('nintendo/price', views.index8, name="allproducts-nintendo-sorted-price"),
    path('nintendo/price/<int:id>', views.get_product_by_id, name="allProduct_details"),
    path('playstation/price', views.index9, name="allproducts-playstation-sorted-price"),
    path('playstation/price/<int:id>', views.get_product_by_id, name="allProduct_details"),
    path('sega/price', views.index10, name="allproducts-sega-sorted-price"),
    path('sega/price/<int:id>', views.get_product_by_id, name="allProduct_details")
]
