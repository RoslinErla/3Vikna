from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="merchandise-index"),
    path('price/', views.index2, name="merchandise-index2")
]