from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(write_only=True)
    is_staff = serializers.BooleanField(required=False)
    is_superuser = serializers.BooleanField(required=False)