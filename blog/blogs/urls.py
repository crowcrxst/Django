"""Определяет схемы URL для BLOGS"""

from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),

    # Страница для добавение нового поста.
    path('new_post/', views.new_post, name='new_post'),

    # Страница для редактирования поста.
    path('edit_post/<int:entry_id>/', views.edit_post, name='edit_post'),
]