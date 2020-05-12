from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="merchandise-index"),
    path('price/', views.index2, name="merchandise-index2"),
    path('nintendo', views.index3, name='merchandise-index3'),
    path('atari', views.index4, name='merchandise-index4', ),
    path('sega', views.index5, name='merchandise-index5'),
    path('playstation', views.index6, name='merchandise-index6'),
    path('atari/price/', views.index7, name='merchandise-atari-sorted-price'),
    path('nintendo/price', views.index8, name='merchandise-nintendo-sorted-price'),
    path('playstation/price', views.index9, name='merchandise-playstation-sorted-price'),
    path('sega/price', views.index10, name='merchandise-sega-sorted-price'),
    path('<int:id>', views.get_product_by_id, name="merchandise_Product_details")

]