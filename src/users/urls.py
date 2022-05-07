from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.api.views import UserView

router = DefaultRouter()
router.register(r'', UserView, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]