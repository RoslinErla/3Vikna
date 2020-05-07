from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="games-index"),
    path('price/', views.index2, name="games-index2")
]