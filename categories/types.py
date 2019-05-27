from graphene_django.types import DjangoObjectType

from .models import Category


class CategoryType(DjangoObjectType):
    """
    Category type implement Category model.
    """

    class Meta:
        model = Category
