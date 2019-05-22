from graphene_django.types import DjangoObjectType
from movies.models import Actor, Movie


class ActorType(DjangoObjectType):
    class Meta:
        model = Actor


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
