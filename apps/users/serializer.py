from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from users.models import UserModel


class UserModelSerializer(ModelSerializer):
    confirm_password = CharField(read_only=True, max_length=255)

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'password', 'username', 'email', 'bio', 'confirm_password']

    def create(self, validated_data):
        password = validated_data['password']
        # validated_data['password'] = make_password(password)
        return super().create(validated_data)

    def update(self, instance, validate_data):
        instance.image = validate_data.get('image', instance.image)
        instance.fullname = validate_data.get('fullname', instance.fullname)
        instance.username = validate_data.get('username', instance.username)
        instance.password = validate_data.get('password', instance.password)
        instance.email = validate_data.get('email', instance.email)
        instance.bio = validate_data.get('bio', instance.bio)

        new_password = validate_data.get('password')
        if new_password:
            instance.password = make_password(new_password)
        instance.save()
        return instance


class UserFollowModelSerializer(ModelSerializer):
    pass


class UserFollowingModelSerializer(ModelSerializer):
    pass


