from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name="User-index"),
    path('login', LoginView.as_view(template_name='admin/login.html'), name="login"),
    path('logout', LogoutView.as_view(next_page='login'), name="logout"),
    path('logout_first', views.logout_first, name="logout_first"),
    path('profile', views.profile, name="profile"),
    path('history', views.browsing_history, name="browsing-history"),
    path('<int:id>', views.get_product_by_id, name="Product_details"),
]
