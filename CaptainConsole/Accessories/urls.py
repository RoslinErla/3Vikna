from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="accessories-index"),
    path('price/', views.index2, name="accessories-index2"),

]