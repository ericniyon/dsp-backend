from django.urls import path, include
from .api import *
from knox import views as knox_view

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/register', RegisterUserAPI.as_view()),
    path('api/auth/login', LoginUserAPI.as_view()),
    path('api/auth/logout', knox_view.LogoutView.as_view()),
]