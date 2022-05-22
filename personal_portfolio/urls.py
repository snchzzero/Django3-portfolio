"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static  # создаем новый юрл шаблон для просмотра изображения
from django.conf import settings  # передает настройки из файла settings
import portfolio.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolio.views.home, name="home"),
    path('blog/', include('blog.urls'), name="blog_click"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # создаем шаблон просмотра картинок на сайте