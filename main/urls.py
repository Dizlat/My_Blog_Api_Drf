from django.urls import path

from main.views import categories

urlpatterns = [
    path('categories/', categories, name='categories-list'),
]