from cgitb import lookup
from dataclasses import fields
from rest_framework import serializers
from ..models import Pet, Expense, Observation, Record
from accounts.models import User
from django.conf import settings

# Customizing token claims
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


###### ONCE ADD IMG URL TO MODELS MUST ADD TO EACH FIELD ON HERE ######

# User = settings.AUTH_USER_MODEL

# Customizing token claims


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username

        return token


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     pets = serializers.HyperlinkedRelatedField(
#         view_name='pet_detail',
#         many=True,
#         read_only=True
#     )

#     class Meta:
#         model = NewUser
#         fields = ('id', 'first_name', 'last_name', 'email',
#                   'location', 'username', 'password', 'pets')


class PetSerializer(serializers.HyperlinkedModelSerializer):

    # user = serializers.HyperlinkedRelatedField(
    #     view_name='user-detail',
    #     read_only=True
    # )

    user = serializers.HyperlinkedIdentityField(
        view_name="accounts:user-detail", read_only=True)

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user'
    )

    expenses = serializers.HyperlinkedRelatedField(
        view_name='expense-detail',
        many=True,
        read_only=True
    )
    observations = serializers.HyperlinkedRelatedField(
        view_name='observation-detail',
        many=True,
        read_only=True
    )
    records = serializers.HyperlinkedRelatedField(
        view_name='record-detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Pet
        fields = ('id', 'user', 'user_id', 'name', 'animal_group',
                  'animal_kind', 'dob', 'gotcha_date', 'age', 'expenses', 'observations', 'records')


class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    pet = serializers.HyperlinkedRelatedField(
        view_name='pet-detail',
        read_only=True,
    )

    pet_id = serializers.PrimaryKeyRelatedField(
        queryset=Pet.objects.all(),
        source='pet'
    )

    class Meta:
        model = Expense
        fields = ('id', 'pet', 'pet_id', 'category',
                  'date', 'amount', 'description')


class ObservationSerializer(serializers.HyperlinkedModelSerializer):
    pet = serializers.HyperlinkedRelatedField(
        view_name='pet-detail',
        read_only=True
    )

    pet_id = serializers.PrimaryKeyRelatedField(
        queryset=Pet.objects.all(),
        source='pet'
    )

    class Meta:
        model = Observation
        fields = ('id', 'pet', 'pet_id',
                  'title', 'date', 'description')


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    pet = serializers.HyperlinkedRelatedField(
        view_name='pet-detail',
        read_only=True
    )

    pet_id = serializers.PrimaryKeyRelatedField(
        queryset=Pet.objects.all(),
        source='pet'
    )

    class Meta:
        model = Record
        fields = ('id', 'pet', 'pet_id', 'clinic_name', 'location',
                  'vet', 'appt_date', 'visit_reason', 'comment')
