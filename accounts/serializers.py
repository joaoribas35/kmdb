from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'password', 'is_staff', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}
