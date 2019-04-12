from rest_framework import viewsets

from .models import User
from .permissions import IsUserOrSignUp
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API View set that perform a CRUD with a user's accounts.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrSignUp,)
