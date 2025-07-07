from rest_framework import viewsets
from .serializer import UsersSerializers
from .models import Users

class UserView (viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers