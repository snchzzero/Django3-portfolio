from django.shortcuts import render, get_object_or_404
# get_object_or_404 - функция позволяющая выгрузить конкретный объект из базы
from .models import Blog

def all_blogs(request):
    # projects = Blog.objects.order_by('-date')[:5]  # на случай если нужно выполнить сортровку по дате
    # и на странице показывать не более 5ти записей
    #projects = Blog.objects.all()  # импорт все даных из базы данных, конвертирует в объекты пайтон и добавляет в список
    projects = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {"projects":projects})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)  # pk-первичный ключ (поиск объекта из базы по номеру ключа)
    return render(request, 'blog/detail.html', {'blog':blog})
