from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="games-index"),
    path('price/', views.index2, name="games-index2"),
    path('nintendo', views.index3, name='games-index3'),
    path('atari', views.index4, name='games-index4', ),
    path('sega', views.index5, name='games-index5'),
    path('playstation', views.index6, name='games-index6'),
    path('<int:id>', views.get_product_by_id, name="games_Product_details")
]
