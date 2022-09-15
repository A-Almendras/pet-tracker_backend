from pyexpat import model
from django.shortcuts import render
from django.http import JsonResponse
from accounts import serializers

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework import generics
from .serializers import PetSerializer, ExpenseSerializer, ObservationSerializer, RecordSerializer, MyTokenObtainPairSerializer
from ..models import Pet, Expense, Observation, Record
from accounts.serializers import RegisterUserSerializer
from accounts.models import User

# Customizing token claims
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.

########### CLASS BASED VIEW ###########
# Customizing token claims
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
########################################


########### FUNCTION BASED VIEW ###########

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def petListByUser(request):
#     user = request.user
#     pets = Pet.objects.filter(user=user)
#     # pets = Pet.objects.all()
#     serializer = PetSerializer(pets, many=True, context={'request': request})
#     return Response(serializer.data)

###########################################



########### CLASS BASED VIEWS ###########

# To view all pets by all users
class PetList(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetListByUser(generics.ListCreateAPIView):
    # queryset = Pet.objects.all()
    model = User
    serializer_class = PetSerializer

    def get_queryset(self):
        user = self.request.user
        return Pet.objects.filter(user=user)


class PetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class ExpenseList(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ObservationList(generics.ListCreateAPIView):
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer


class ObservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer


class RecordList(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
########################################

#####DELETE IF APP ENDS UP WORKING######
# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterUserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterUserSerializer

########################################