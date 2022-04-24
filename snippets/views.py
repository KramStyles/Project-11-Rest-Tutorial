from rest_framework import generics, response, decorators, status

from . import serializers
from .models import Snippet


class ViewApi(generics.ListCreateAPIView):
    serializer_class = serializers.SnippetSerializers
    queryset = Snippet.objects.all()


class ViewModelApi(generics.ListCreateAPIView):
    serializer_class = serializers.SnippetSerializers
    queryset = Snippet.objects.all()


@decorators.api_view(['GET', 'POST'])
def snips(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = serializers.SnippetSerializers(snippets, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = serializers.SnippetModel(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    # Create your views here.
