from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)  # в заголовках небольше 200символов
    description = models.TextField()
    image = models.ImageField(upload_to="blog/images/")
    url = models.URLField(blank=True)  # открываем страницу (сылку) на новой вкладке браузера
    date = models.DateField()

    def __str__(self):  # функция в отображении панели админа возращает не номера проектов, а заголовок проекта
        return self.title

