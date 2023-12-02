from django.db import models
from django.utils import timezone


class Worker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.SmallIntegerField(null=True)
    created = models.DateTimeField(default=timezone.now)
    work_experience = models.SmallIntegerField(default=0)


class Publisher(models.Model):  # наследуем от Model
    name = models.CharField(max_length=30)  # имя, строка (макс. Длина=30)
    address = models.CharField(max_length=50)  # адрес, строка (макс.Длина = 50)
    city = models.CharField(max_length=60)  # город, строка (макс. Длина=60)
    state_province = models.CharField(max_length=30)  # область, строка (макс.Длина = 30)
    country = models.CharField(max_length=50)  # страна, строка (макс.Длина = 50)
    website = models.URLField()  # сайт, URL


class Author(models.Model):
    first_name = models.CharField(max_length=30)  # имя, строка (макс.Длина = 30)
    last_name = models.CharField(max_length=40)  # фамилия, строка (макс.Длина = 40)
    email = models.EmailField()  # эл. почта, Email


class Book(models.Model):
    title = models.CharField(max_length=100)  # название (макс. Длина=100)
    authors = models.ManyToManyField(Author)  # поле многие-ко-многим
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)  # FK на Publisher
    publication_date = models.DateField()  # дата публикации
