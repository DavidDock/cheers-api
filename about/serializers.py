from rest_framework import serializers
from about.models import About


class AboutSerializer(serializers.ModelSerializer):
    """
    Serializer for the About model
    """

    class Meta:
        model = About
        fields = ['id', 'created_at', 'title', 'content']