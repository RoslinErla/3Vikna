from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="accessories-index"),
    path('price/', views.index2, name="accessories-index2"),
    path('nintendo', views.index3, name='accessories-index3'),
    path('atari', views.index4, name='accessories-index4',),
    path('sega', views.index5, name='accessories-index5'),
    path('playstation', views.index6, name='accessories-index6'),
    path('atari/price/', views.index7, name='accessories-atari-sorted-price'),
    path('nintendo/price', views.index8, name='accessories-nintendo-sorted-price'),
    path('playstation/price', views.index9, name='accessories-playstation-sorted-price'),
    path('sega/price', views.index10, name='accessories-sega-sorted-price'),
    path('<int:id>', views.get_product_by_id, name="accessories_Product_details"),
]