from django.urls import path, include
from rest_framework.routers import DefaultRouter

from content.views import PostModelSetView

router = DefaultRouter()
router.register('p', PostModelSetView, basename='posts')
urlpatterns = [
    path('', include(router.urls))
]
