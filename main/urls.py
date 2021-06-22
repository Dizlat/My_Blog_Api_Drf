from django.urls import path

from main.views import *

urlpatterns = [
    path('categories/', categories, name='categories-list'),
    path('posts/', PostListView.as_view(), name='posts-list'),

]