from rest_framework import serializers
from . import models

class HelloSearilizer(serializers.Serializer):
    """Serializes a name field for testing our api view"""
    name = serializers.CharField(max_length=10)
    

class UserProfileSerializers(serializers.ModelSerializer):
    """Serializes a User Profile object"""

    class Meta:
        model = models.UserProfile
        fields =('id','email','name','password')
        extra_kwargs = {
            'password' : {
                'write_only' : True,
                'style': {'input_type':'password'}
            }
        }
    
    def create(self, validated_data):
        '''Create and return a new User'''
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'],
        )
        return user
