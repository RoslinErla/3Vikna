from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="consoles-index"),
    path('', views.index2, name="consoles-index2"),
    path('nintendo', views.index3, name='consoles-index3'),
    path('atari', views.index4, name='consoles-index4',),
    path('sega', views.index5, name='consoles-index5'),
    path('playstation', views.index6, name='consoles-index6')
]
