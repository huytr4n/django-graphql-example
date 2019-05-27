from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Category Serializer."""

    class Meta:
        """Category Serializer meta data."""

        model = Category
        fields = '__all__'
