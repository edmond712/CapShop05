from rest_framework import serializers
from .models import MyUser


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('phone_number', 'username', 'password')

    def create(self, validated_data):
        user = MyUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            if field == 'password':
                instance.set_password(value)
            else:
                setattr(instance, field, value)
        instance.save()
        return instance


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('id', 'cover', 'username', 'phone_number', 'email', 'address')


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('cover', 'username', 'phone_number', 'email', 'address')

