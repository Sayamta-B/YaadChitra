from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'phone_number']
        extra_kwargs={
            'username':{'required':True},
            'email':{'required':True},
            'password':{'required':True},
            'first_name':{'required':True},
            'last_name':{'required':True},
            'phone_number':{'required':True},
            'email':{'required':True},
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'phone_number',
        ]
        read_only_fields = ['id', 'username']