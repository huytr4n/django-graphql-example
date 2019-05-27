import graphene
from graphene_django.types import ObjectType

from .types import CategoryType
from .models import Category


class Query(ObjectType):
    """
    Query class.
    """

    category = graphene.Field(CategoryType, id=graphene.Int())
    categories = graphene.List(CategoryType)

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Category.objects.get(pk=id)

        return None

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()
