from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from . import serializers as S

class UserViewSet(viewsets.ModelViewSet):
    """Api endpoint that allows user to be viewed or edited"""
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = S.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """Api endpoint that allows groups to be viewed or edited"""
    queryset = Group.objects.all()
    serializer_class = S.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
