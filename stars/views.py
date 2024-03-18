from rest_framework import generics, permissions
from cheers_api.permissions import IsOwnerOrReadOnly
from stars.models import Star
from stars.serializers import StarSerializer


class StarList(generics.ListCreateAPIView):
    """
    List stars or create a star if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StarSerializer
    queryset = Star.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StarDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a star or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = StarSerializer
    queryset = Star.objects.all()
