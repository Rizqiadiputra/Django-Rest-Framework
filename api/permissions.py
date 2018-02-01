from rest_framework.permissions import BasePermission
from .models import DataList

class IsOwner(BasePermission):
    """Custom perizinan kelas untuk  mengizinkan hanya owner datalist
    yang bisa edit itu """

    def has_object_permission(self, request, view, obj):
        """Pengembalian Benar jika perizinan dikabulkan untuk owner datalist"""
        if isinstance(obj, DataList):
            return obj.owner == request.user
        return obj.owner == request.user

    """
    The class above implements a permission which holds by this truth – 
    The user has to be the owner to have that object's permission. 
    If they are indeed the owner of that bucketlist, it returns True, else False.

    """