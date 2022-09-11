from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.response import Response
from .models import User
from .serializers import RegisterUserSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class CreateUserView(CreateAPIView):
    created = {'status': '201 Created: Request Created'}
    denied = {'status': '400 Bad Request: Request Denied'}
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterUserSerializer
    # def post(self, request):
    #     serializer_class = RegisterNewUserSerializer(data=request.data)
    #     if serializer_class.is_valid():
    #         newuser = serializer_class.save()
    #         if newuser:
    #             return Response(created)
    #     return Response(serializer_class.errors, denied)


class UserList(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = RegisterUserSerializer


class UserDetail(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = RegisterUserSerializer
