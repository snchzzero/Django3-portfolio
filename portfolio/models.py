from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)  # в заголовках небольше 100символов
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="portfolio/images/")
    url = models.URLField(blank=True)  # открываем страницу (сылку) на новой вкладке браузера

    def __str__(self):  # функция в отображении панели админа возращает не номера проектов, а заголовок проекта
        return self.title