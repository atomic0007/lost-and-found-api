from django.shortcuts import render

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import generics
from .serializers import CustomUserSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer

class LoginView(TokenObtainPairView):
    pass

