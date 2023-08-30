from django.shortcuts import render
from django.utils.decorators import method_decorator
from drf_yasg import openapi, utils
from rest_framework.viewsets import ModelViewSet


@method_decorator(name='create', decorator=utils.swagger_auto_schema(manual_parameters=[openapi.Parameter(
    name='media',
    in_=openapi.IN_FORM,
    type=openapi.TYPE_ARRAY,
    items=openapi.Items(type=openapi.TYPE_FILE),
    required=True,
    description='media'
)]))


class PostModelSetView(ModelViewSet):
    pass



