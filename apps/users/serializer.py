from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, HiddenField, CurrentUserDefault
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from users.models import UserModel


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'password', 'username', 'email', 'bio']

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


class UserViewProfileModelSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'first_name', 'username', 'image')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context['request']
        data['is_followed'] = False
        if request and (user := getattr(request, 'user')) and user.is_authenticated:
            data['is_followed'] = user.following.filter(id=instance.id).exists()
        return data


class UserFollowModelSerializer(ModelSerializer):
    followers = UserViewProfileModelSerializer(many=True)
    following = UserViewProfileModelSerializer(many=True)

    class Meta:
        model = UserModel
        fields = ('following', 'followers')


class UserFollowingModelSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())
    follow_user_id = PrimaryKeyRelatedField(queryset=UserModel.objects.all())

    class Meta:
        model = UserModel
        fields = ('follow_user_id', 'user')

    def create(self, validated_data):
        user: UserModel = validated_data['user']
        follow_user = validated_data['follow_user_id']
        if user.following.filter(id=follow_user.id).first():
            user.following.remove(follow_user)
            follow_user.followers.remove(user)
            follow_user.save()
            user.save()
        else:
            user.following.add(follow_user)
            user.save()
            follow_user.followers.add(user)
            follow_user.save()
        return user

    def to_representation(self, instance):
        return {'message': "you've followed successfully"}



