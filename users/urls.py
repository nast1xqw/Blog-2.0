from django.urls import path
from users.views import (
    login_view,
    logout_view, 
    profile_view, 
    register_view,
)


urlpatterns =[
    path('login/', login_view, name='users-login'),
    path('logout/', logout_view, name='users-logout'),
    path('profile/', profile_view, name='users-profile'),
    path('register/', register_view, name='users-register'),

]