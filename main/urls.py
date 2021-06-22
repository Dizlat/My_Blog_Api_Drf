from django.urls import path

from main.views import *

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories-list'),
    path('posts/', PostListView.as_view(), name='posts-list'),
    path('post-create/', PostCreateView.as_view(), name='post-create'),

]