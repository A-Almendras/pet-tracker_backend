from dataclasses import fields
from rest_framework import serializers
from ..models import Pet, Expense, Observation, Record
from accounts.models import NewUser

# Customizing token claims
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


###### ONCE ADD IMG URL TO MODELS MUST ADD TO EACH FIELD ON HERE ######

# Customizing token claims
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

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
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
    expenses = serializers.HyperlinkedRelatedField(
        view_name='expense_detail',
        many=True,
        read_only=True
    )
    observations = serializers.HyperlinkedRelatedField(
        view_name='observation_detail',
        many=True,
        read_only=True
    )
    records = serializers.HyperlinkedRelatedField(
        view_name='record_detail',
        many=True,
        read_only=True
    )

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=NewUser.objects.all(),
        source='user'
    )

    class Meta:
        model = Pet
        fields = ('id', 'user', 'user_id', 'name', 'animal_group',
                  'animal_kind', 'dob', 'gotcha_date', 'age', 'expenses', 'observations', 'records')


class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    pet = serializers.HyperlinkedRelatedField(
        view_name='pet_detail',
        read_only=False,
        queryset=Pet.objects.all()
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
        view_name='pet_detail',
        read_only=True
    )

    pet_id = serializers.PrimaryKeyRelatedField(
        queryset=Pet.objects.all(),
        source='pet'
    )

    class Meta:
        model = Observation
        fields = ('id', 'pet', 'pet_id', 'title', 'date', 'description')


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    pet = serializers.HyperlinkedRelatedField(
        view_name='pet_detail',
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
