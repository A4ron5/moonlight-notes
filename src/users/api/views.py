
from rest_framework.viewsets import ReadOnlyModelViewSet

from users.api.serializers import UserSerializer
from users.models import User


class UserView(ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

