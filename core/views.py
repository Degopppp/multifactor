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
    logout(request)          # Cierra sesión en Django
    request.session.flush()  # Elimina todos los datos de sesión

    # Redirige a cierre de sesión de Google, y de vuelta a tu 'root'
    return redirect(
        'https://accounts.google.com/Logout?continue=https://appengine.google.com/_ah/logout?continue=http://localhost:8000/'
    )