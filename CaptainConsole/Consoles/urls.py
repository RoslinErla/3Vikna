from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="consoles-index"),
    path('', views.index2, name="consoles-index2")
]