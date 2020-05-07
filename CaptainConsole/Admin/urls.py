from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name="Admin-index"),
    path('login', Loginview.as_view(template_name='admin/login.html',name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name = 'logout')]