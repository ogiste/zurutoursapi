from rest_framework import serializers
from .models import User

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'id', 'username', 'first_name', 'last_name', 'phone', 'email', 'password')
        read_only_fields = ('updatedOn', 'createdOn')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data.get("password"))
        user.save()
        return user