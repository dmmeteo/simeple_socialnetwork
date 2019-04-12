from rest_framework import serializers
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('url', 'id', 'email', 'password',)
        read_only_fields = ('url', 'id',)
        extra_kwargs = {'password': {'write_only': True}}

