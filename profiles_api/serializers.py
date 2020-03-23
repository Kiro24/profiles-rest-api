from rest_framework import serializers
from django.contrib.auth import get_user_model

class HelloSerializer(serializers.Serializer):
    """Acts as django forms to handle validation of python/JSON data accross api"""
    name = serializers.CharField(max_length=10)



class UserProfileSerializer(serializers.ModelSerializer):
    '''Serializes a user profile object'''

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        '''creates and returns a new user object'''

        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user