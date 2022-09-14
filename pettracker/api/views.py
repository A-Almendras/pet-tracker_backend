from django.shortcuts import render
from rest_framework import generics
from .serializers import PetSerializer, ExpenseSerializer, ObservationSerializer, RecordSerializer, MyTokenObtainPairSerializer
from ..models import Pet, Expense, Observation, Record
from accounts.serializers import RegisterUserSerializer
from accounts.models import User

# Customizing token claims
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.


# Customizing token claims
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

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


class PetList(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetListByuser(generics.ListCreateAPIView):
    # queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def get_queryset(self):
        return self.model.objects.owned_by_user(self.request.user)


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
