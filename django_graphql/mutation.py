import os
import graphene
import importlib
import environ

from inspect import getmembers, isclass
from django.conf import settings

env = environ.Env()


class MutationsAbstract(graphene.ObjectType):
    pass


mutations_base_classes = [MutationsAbstract]
current_directory = os.path.dirname(os.path.abspath(__file__))
root_directory = environ.Path(__file__) - 2  # (/a/myfile.py - 1 = /)
current_module = str(root_directory).split('/')[-1]
subdirectories = [
    x
    for x in os.listdir(root_directory)
    if os.path.isdir(os.path.join(root_directory, x)) and
    x != '__pycache__'
]
for directory in subdirectories:
    if directory in settings.GRAPHQL_APPS:
        try:
            module = importlib.import_module(f'{directory}.mutations')
            if module:
                classes = [x for x in getmembers(module, isclass)]
                mutations = [x[1] for x in classes if 'SMutation' in x[0]]
                mutations_base_classes += mutations
        except ModuleNotFoundError:
            pass

mutations_base_classes = mutations_base_classes[::-1]
properties = {}
for base_class in mutations_base_classes:
    properties.update(base_class.__dict__['_meta'].fields)

Mutations = type(
    'Mutations',
    tuple(mutations_base_classes),
    properties
)
