from rest_framework import generics, response

from .serializers import SnippetSerializers
from .models import Snippet

class ViewApi(generics.ListCreateAPIView):
    serializer_class = SnippetSerializers
    queryset = Snippet.objects.all()

    
# Create your views here.
