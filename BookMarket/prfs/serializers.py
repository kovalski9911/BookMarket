from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Prf


User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for model Prf"""

    class Meta:
        model = Prf
        fields = ('delivery_address', 'phone_number')


class UserSerializer(serializers.ModelSerializer):
    """Serializer for model User"""
    prf = ProfileSerializer()

    class Meta:
        model = User
        fields = ('username', 'email', 'prf')

    def update(self, instance, validated_data):
        prf_data = validated_data.pop('prf')
        prf = instance.prf

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        prf.delivery_address = prf_data.get(
            'delivery_address',
            prf.delivery_address
        )
        prf.phone_number = prf_data.get(
            'phone_number',
            prf.phone_number
        )
        prf.save()

        return instance


class RegisterUserSerializer(serializers.ModelSerializer):
    """Serializer for register users"""

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
