from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import MovieSerializer, MovieMiniSerializer
from .models import Movie
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class MySampleView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(data={"status":True})

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def list(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = MovieMiniSerializer(movies, many=True)
        return Response(serializer.data)


