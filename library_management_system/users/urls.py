from django.urls import path
from .views import register
from django.contrib.auth import views as auth_views
from books import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', register, name='register'),
    path('profile/', views.user_profile_and_books, name='profile'),
]
