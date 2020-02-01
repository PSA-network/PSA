"""
Definition of models.
"""

from django.db import models
from datetime import datetime
from django.contrib import admin #добавили использование административногомодуля
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User #для импорта авторакомментариев

# Модель данных Блога
class Blog(models.Model):
 title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name
= "Заголовок")
 description = models.TextField(verbose_name = "Краткое содержание")
 content = models.TextField(verbose_name = "Полное содержание")
 posted = models.DateTimeField(default = datetime.now(), db_index = True,
 verbose_name = "Опубликована")
 image = models.FileField(default = 'temp.jpg', verbose_name = "Путь к картинке") #модель записи блога поле для картинки
 def get_absolute_url(self): # метод возвращает строку с уникальным интернет адресом записи
      return reverse("blogpost", kwargs = {"pk": self.pk})
 def __str__(self): # метод возвращает название, используемое дляпредставления отдельных записей в административном разделе
      return self.title
 class Meta:  # метаданные – вложенный класс, который задаетдополнительные параметры модели:
     db_table = "Posts" # имя таблицы для модели
     ordering = ["-posted"] # порядок сортировки данных в модели ("-" означаетпо убыванию)
     verbose_name = "статья блога" # имя, под которым модель будетотображаться в административном разделе (для одной статьи блога)
     verbose_name_plural = "статьи блога" # тоже для всех статей блога
admin.site.register(Blog)
# Модель комментариев
class Comment(models.Model):
  text = models.TextField(verbose_name = "Комментарий")
  date = models.DateTimeField(default = datetime.now(), db_index = True,
  verbose_name = "Дата")
  author = models.ForeignKey(User, on_delete = models.CASCADE,
  verbose_name = "Автор") # из модели User (вторичный ключ), каскадноеудаление записей в обоих таблицах
  post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name ="Статья") # из модели Blog (вторичный ключ), каскадное удалениезаписей в обоих таблицах
  class Meta: # метаданные – вложенный класс, который задает дополнительные параметры модели:
   db_table = "Comments" # имя таблицы для модели
   verbose_name = "Комментарий"
   verbose_name_plural = "Комментарии статьи блога"
   ordering = ["-date"]
admin.site.register(Comment)
class News(models.Model):
 title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name
= "Заголовок")
 description = models.TextField(verbose_name = "Краткое содержание")
 content = models.TextField(verbose_name = "Полное содержание")
 posted = models.DateTimeField(default = datetime.now(), db_index = True,
 verbose_name = "Опубликована")
 #image = models.FileField(default = 'temp.jpg', verbose_name = "Путь к картинке") #модель записи блога поле для картинки
 def get_absolute_url(self): # метод возвращает строку с уникальным интернет адресом записи
      return reverse("news", kwargs = {"pk": self.pk})
 def __str__(self): # метод возвращает название, используемое дляпредставления отдельных записей в административном разделе
      return self.title
 class Meta:  # метаданные – вложенный класс, который задаетдополнительные параметры модели:
     db_table = "News" # имя таблицы для модели
     ordering = ["-posted"] # порядок сортировки данных в модели ("-" означаетпо убыванию)
     verbose_name = "новость" # имя, под которым модель будетотображаться в административном разделе (для одной статьи блога)
     verbose_name_plural = "новости" # тоже для всех статей блога
admin.site.register(News)

# Модель заявок
class Orders(models.Model):
  title = models.CharField(max_length = 100, verbose_name = "Тема")
  text = models.TextField(verbose_name = "Заявка")
  date = models.DateTimeField(default = datetime.now(), db_index = True,
  verbose_name = "Дата")
  author = models.ForeignKey(User, on_delete = models.CASCADE,
  verbose_name = "Автор", related_name="author") # из модели User (вторичный ключ), каскадноеудаление записей в обоих таблицах
  status = models.PositiveIntegerField(verbose_name = "Статус")
  changeddate = models.DateTimeField(default = datetime.now(), db_index = True,
  verbose_name = "Дата изменения")
  changeduser = models.ForeignKey(User, on_delete = models.CASCADE,
  verbose_name = "Кто изменил", related_name="changed_user", blank=True, null=True)
  class Meta: # метаданные – вложенный класс, который задает дополнительные параметры модели:
   db_table = "Orders" # имя таблицы для модели
   verbose_name = "заявка"
   verbose_name_plural = "заявки"
   ordering = ["-date"]
admin.site.register(Orders)

# Create your models here.
