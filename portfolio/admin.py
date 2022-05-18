from django.contrib import admin
from .models import Project  # импортируем модели из модельс

admin.site.register(Project)  # зарегистрируем импортированные модели в админке
