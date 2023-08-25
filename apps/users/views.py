from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from users.models import UserModel
from users.serializer import UserModelSerializer, UserFollowModelSerializer, UserFollowingModelSerializer


class UserModelSetView(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = (AllowAny, )
    # permission_classes = (UserModelPermissions, )


class UserFollowModelViewSet(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserFollowModelSerializer
    http_method_names = ['get', 'post']

    def get_serializer_class(self):
        if self.action == 'create':
            return UserFollowingModelSerializer
        return super().get_serializer_class()


