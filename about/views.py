from rest_framework import generics, permissions
from .models import About
from .serializers import AboutSerializer


class AboutList(generics.ListAPIView):
    """
    List abouts
    """
    serializer_class = AboutSerializer
    queryset = About.objects.all()
