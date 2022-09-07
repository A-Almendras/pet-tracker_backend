# from rest_framework import serializers
# from django.contrib.auth import get_user_model
# from .models import NewUser
# # from pettracker.serializers import PetSerializer


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     pets = serializers.HyperlinkedRelatedField(
#         view_name='pet_detail',
#         many=True,
#         read_only=True
#     )

#     def create(self, validated_data):
#         user = NewUser.objects.create_user(
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name'],
#             email=validated_data['email'],
#             location=validated_data['location'],
#             username=validated_data['username'],
#             password=validated_data['password'],
#         )
#         return user

#     class Meta:
#         model = NewUser
#         fields = ('id', 'first_name', 'last_name', 'email',
#                   'location', 'username', 'password', 'pets')
