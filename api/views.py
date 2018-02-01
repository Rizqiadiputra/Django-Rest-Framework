from django.shortcuts import render
from rest_framework import permissions, generics
from .permissions import IsOwner
from .serializers import DataListSerializer, UserSerializer
from .models import DataList
from django.contrib.auth.models import User

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    """Kelas ini mendifinisikan pembuatan perilaku
    dari rest api kita
    kelas ini menangani Get dan Post yang di request pada rest API kita
    """

    queryset = DataList.objects.all()
    serializer_class = DataListSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """Simpan post data saat pembuatan datalist baru"""
        # serializer.save()
        serializer.save(owner=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Kelas ini menangani permintaan http GET, PUT, dan Delete"""

    queryset = DataList.objects.all()
    serializer_class = DataListSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

"""
You can think of authentication as a way to verify someone's identify. 
(username, password, tokens, keys et cetera) and 
authorization as a method that determines the level of access 
a verified user should be granted.
"""

class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer