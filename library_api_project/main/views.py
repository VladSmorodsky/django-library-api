from typing import List

from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend

from main.filters import BookFilter
from main.models import Book
from main.serializers import BookSerializer, RegisterUserSerializer


# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    """
    Endpoint for viewing and editing books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookFilter

    def get_permissions(self) -> List[permissions.BasePermission]:
        """
        Get permissions for destroying books only for admins
        :return:
        """
        if self.action == 'destroy':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class RegisterUserViewSet(viewsets.ModelViewSet):
    """
    Register new users
    """
    serializer_class = RegisterUserSerializer
    permission_classes = [permissions.AllowAny]
