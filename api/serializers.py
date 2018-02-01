"""
Serializing mengubah data dari querysets yang kompleks dari DB
ke bentuk data yang bisa kita pahami, seperti JSON atau XML.
 Deserializing mengembalikan proses ini setelah
  memvalidasi data yang ingin kita simpan ke DB.
"""

from rest_framework import serializers
from .models import DataList
from django.contrib.auth.models import User

class DataListSerializer(serializers.ModelSerializer):
    """Serializer untuk memetakan model instance ke format JSON"""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Kelas Meta untuk memetakan kolom serializer dengan kolom dalam model"""
        model = DataList
        fields = ('id', 'name', 'owner', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    datalists = serializers.PrimaryKeyRelatedField(many=True, queryset=DataList.objects.all())

    """Map this serializer to the default django user model."""
    class Meta:
        model = User
        fields = ('id', 'username', 'datalists')