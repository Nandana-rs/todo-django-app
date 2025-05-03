from django.urls import path
from . import views
from .views import TaskListView, TaskCreateView
from .views import logout_view

from .views import TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', views.homepage ,name='homepage'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('user_home/', views.user_home_view, name='user_home'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('tasks/',TaskListView.as_view(), name='task-list'),
    path('tasks/create', TaskCreateView.as_view(), name='task-create'),
    path('logout/', views.logout_view, name='logout'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task-edit'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('important-tasks/', views.important_tasks, name='important-tasks'),



]