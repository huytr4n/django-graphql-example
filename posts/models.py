# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    """
    Model Category.
    """

    name = models.CharField(("Category's name"), max_length=50)
    description = models.CharField(("Category's description"), max_length=100)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categorys")


class Post(models.Model):
    """
    Model Post.
    """

    content = models.TextField(("Post's content"))
    time = models.DateTimeField(("Post time"), auto_now=False, auto_now_add=False)
    url = models.CharField(("Post's URL"), max_length=50)
    category = models.ForeignKey(Category, verbose_name=("Category ID"), on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")
