from rest_framework import generics, permissions
from cheers_api.permissions import IsOwnerOrReadOnly
from cheers.models import Cheer
from cheers.serializers import CheerSerializer


class CheerList(generics.ListCreateAPIView):
    """
    List cheers or create a cheer if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CheerSerializer
    queryset = Cheer.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CheerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a cheer or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CheerSerializer
    queryset = Cheer.objects.all()
