import os
import graphene
import importlib
import environ

from inspect import getmembers, isclass
from django.conf import settings

env = environ.Env()


class QueriesAbstract(graphene.ObjectType):
    pass


queries_base_classes = [QueriesAbstract]
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
            module = importlib.import_module(f'{directory}.queries')
            if module:
                classes = [x for x in getmembers(module, isclass)]
                queries = [x[1] for x in classes if 'Query' in x[0]]
                queries_base_classes += queries
        except ModuleNotFoundError:
            pass

queries_base_classes = queries_base_classes[::-1]
properties = {}
for base_class in queries_base_classes:
    properties.update(base_class.__dict__['_meta'].fields)

Queries = type(
    'Queries',
    tuple(queries_base_classes),
    properties
)
