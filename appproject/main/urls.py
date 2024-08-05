from django.urls import path

from .views import *

urlpatterns = [
    path('', MainHomeView.as_view(), name='index'),
    path('profile/', profile_page, name='profile'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]