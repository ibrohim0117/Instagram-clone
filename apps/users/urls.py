from rest_framework.routers import DefaultRouter
from django.urls import path, include

from users.views import UserModelSetView

router = DefaultRouter()
router.register("users", UserModelSetView, basename="users")

urlpatterns = [
    path('', include(router.urls))
]