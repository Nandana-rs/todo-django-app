from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage ,name='homepage'),
     path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('user_home/', views.user_home_view, name='user_home'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]