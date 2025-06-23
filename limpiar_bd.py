# limpiar_bd.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'multifactor.settings')  # Cambia 'multifactor' si tu proyecto se llama distinto
django.setup()

from django.apps import apps

for model in apps.get_models():
    model.objects.all().delete()
    print(f"✔ Datos eliminados de {model.__name__}")
