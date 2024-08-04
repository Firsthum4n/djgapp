from django.urls import path

from .views import *

urlpatterns = [
    path('', MainHomeView.as_view(), name='index'),
    path('profile/', profile_page, name='profile'),
    path('login/', login_page, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
]