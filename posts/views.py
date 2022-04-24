from rest_framework import generics, permissions

from . import serializers
from .models import Post
from . import permissions as P


class PostList(generics.ListCreateAPIView):
    serializer_class = serializers.PostSerializers

    def get_queryset(self):
        return Post.objects.all()


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [P.IsAuthorOrReadOnly]
    serializer_class = serializers.PostSerializers
    queryset = Post.objects.all()
