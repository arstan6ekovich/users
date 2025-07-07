from rest_framework import viewsets, generics
from .serializer import UsersSerializers
from .models import Users

class UserView (generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers