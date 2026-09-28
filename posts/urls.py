from django.urls import path
from posts.views import create_post

urlpatterns =[
    path('create/', create_post, name='posts-create'),

]