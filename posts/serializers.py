from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """Post Serializer."""

    class Meta:
        """Post Serializer meta data."""

        model = Post
        fields = '__all__'
