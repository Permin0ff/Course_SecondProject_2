from django.urls import path
from orm_method import views

urlpatterns = [path("", views.index, name="index"), ]