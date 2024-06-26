from rest_framework import generics, permissions
from .models import Contact
from .serializers import ContactSerializer


class ContactCreate(generics.CreateAPIView):
    """
    Create contact messages
    """
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
