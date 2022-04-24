from rest_framework import generics

from . import serializers
from .models import Post


class PostList(generics.ListCreateAPIView):
    serializer_class = serializers.PostSerializers

    def get_queryset(self):
        return Post.objects.all()
