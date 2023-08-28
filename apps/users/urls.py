from rest_framework.routers import DefaultRouter
from django.urls import path, include

from users.views import UserModelSetView, UserFollowModelViewSet

router = DefaultRouter()
router.register("users", UserModelSetView, basename="users")
router.register("follow", UserFollowModelViewSet, basename="follow")

urlpatterns = [
    path('', include(router.urls))
]