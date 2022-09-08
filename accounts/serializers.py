from rest_framework import serializers
from django.contrib.auth import get_user_model
# from .models import NewUser
# from pettracker.serializers import PetSerializer

# Returns the model defined in AUTH_USER_MODEL
User = get_user_model()


# Makes the data in an acceptable format to be entered/utilized/saved into the db
class RegisterNewUserSerializer(serializers.ModelSerializer):

    #  Validation of user
    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
        )
        # password = validated_data('password', None)
        # instance = self.Meta.model(**validated_data)
        # if password is not None:
        #   instance.set_password(password)
        # instance.save)
        # return instance
        return user

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name',
                  'email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}
