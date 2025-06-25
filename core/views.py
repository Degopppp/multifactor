from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def login_view(request):
    return render(request, 'core/login.html')

def login_google_redirect(request):
    return redirect('/oauth/login/google-oauth2/')

@login_required
def home_view(request):
    return render(request, 'core/home.html')

def logout_view(request):
    logout(request)
    # Redirige a Google para cerrar sesión globalmente
    return redirect('https://accounts.google.com/Logout?continue=https://appengine.google.com/_ah/logout?continue=http://127.0.0.1:8000/')