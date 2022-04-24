from rest_framework import generics, permissions

from . import serializers
from .models import Post


class PostList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.PostSerializers

    def get_queryset(self):
        return Post.objects.all()


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.PostSerializers
    queryset = Post.objects.all()
