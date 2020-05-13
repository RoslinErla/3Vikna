from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="games-index"),
    path('price/', views.index2, name="games-index2"),
    path('price/<int:id>', views.get_product_by_id, name="games_Product_details"),
    path('nintendo', views.index3, name='games-index3'),
    path('nintendo/<int:id>', views.get_product_by_id, name="games_Product_details"),
    path('nintendo/price', views.index8, name='games-nintendo-sorted-price'),
    path('nintendo/price/<int:id>', views.get_product_by_id, name="games_Product_details"),
    path('atari', views.index4, name='games-index4', ),
    path('atari/<int:id>', views.get_product_by_id, name="games_Product_details"),
    path('sega', views.index5, name='games-index5'),
    path('sega/<int:id>', views.get_product_by_id, name="games_Product_details"),
    path('sega/price', views.index10, name='games-sega-sorted-price'),
    path('sega/price/<int:id>', views.get_product_by_id, name="games_Product_details"),
    path('playstation', views.index6, name='games-index6'),
    path('playstation/<int:id>', views.get_product_by_id, name="games_Product_details"),
    path('playstation/price', views.index9, name='games-playstation-sorted-price'),
    path('playstatioin/price/<int:id>', views.get_product_by_id, name="games_Product_details"),
    path('atari/price/', views.index7, name='games-atari-sorted-price'),
    path('atari/price/<int:id>', views.get_product_by_id, name="games_Product_details"),
    path('<int:id>', views.get_product_by_id, name="games_Product_details"),
]
