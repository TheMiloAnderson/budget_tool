from django.urls import path
from .views import UserAPIView, RegisterAPIView
from rest_framework.authtoken import views


urlpatterns = [
    path('user/<int:pk>', UserAPIView.as_view()),
    path('register', RegisterAPIView.as_view()),
    path('login', views.obtain_auth_token)
]
