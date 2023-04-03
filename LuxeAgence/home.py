from django.shortcuts import render
from django.contrib.auth import views as auth_views #new
from django.conf import settings
import os

def index(request):
    template_path = os.path.join(settings.BASE_DIR, 'Agence/templates/index.html')
    return render(request, template_path, {})