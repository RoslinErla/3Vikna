from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="consoles-index"),
    path('price', views.index2, name="consoles-index2"),
    path('nintendo', views.index3, name='consoles-index3'),
    path('atari', views.index4, name='consoles-index4',),
    path('sega', views.index5, name='consoles-index5'),
    path('playstation', views.index6, name='consoles-index6'),
    path('<int:id>', views.get_product_by_id, name="consoles_Product_details"),
    path('atari/price', views.index7, name="consoles-atari-sorted-price"),
    path('playstation/price', views.index8, name="consoles-playstation-sorted-price"),
    path('sega/price', views.index9, name="consoles-sega-sorted-price"),
    path('nintendo/price', views.index10, name="consoles-nintendo-sorted-price")
]
