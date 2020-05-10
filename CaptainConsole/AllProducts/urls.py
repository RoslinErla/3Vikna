from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="allProducts-index"),
    path('price/', views.index2, name="allProducts-index2"),
    path('nintendo/', views.index3, name="allProducts-index3"),
    path('atari/', views.index4, name="allProducts-index4"),
    path('sega_genesis/', views.index5, name="allProducts-index5"),
    path('playstation/', views.index6, name="allProducts-index6"),
    path('<int:id>', views.get_product_by_id, name="allProduct_details")
]