from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from core import views

urlpatterns = [
    path('', views.login_view, name='root'),
    path('login-google/', views.login_google_redirect, name='login_google'),
    path('admin/', admin.site.urls),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('oauth/', include('social_django.urls', namespace='social')),  # Google OAuth 2.0
    
]
