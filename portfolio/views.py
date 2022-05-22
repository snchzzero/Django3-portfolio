from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()  # импорт все даных из базы данных, конвертирует в объекты пайтон и добавляет в список
    return render(request, "portfolio/home.html", {'projects':projects})

# Create your views here.
