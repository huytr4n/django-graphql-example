from graphene_django.rest_framework.mutation import SerializerMutation

from .serializers import CategorySerializer


class Mutation(SerializerMutation):
    """
    Mutation reuse serializer from DRF
    """

    class Meta:
        serializer_class = CategorySerializer
        model_operations = ['create', 'update']
        lookup_field = 'id'
