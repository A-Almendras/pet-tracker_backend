from urllib import request
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.response import Response

from .serializers import RegisterNewUserSerializer

# Create your views here.


class CreateNewUserView(CreateAPIView):
    created = {'status': '201 Created: Request Created'}
    denied = {'status': '400 Bad Request: Request Denied'}
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterNewUserSerializer

    # def post(self, request):
    #     serializer_class = RegisterNewUserSerializer(data=request.data)
    #     if serializer_class.is_valid():
    #         newuser = serializer_class.save()
    #         if newuser:
    #             return Response(created)
    #     return Response(serializer_class.errors, denied)
