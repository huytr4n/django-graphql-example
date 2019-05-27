from django.db import models

from categories.models import Category


class Post(models.Model):

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated at"
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Is published?"
    )
    published_at = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
        verbose_name="Published at"
    )
    category = models.ForeignKey(
        Category,
        verbose_name="Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    title = models.CharField(max_length=200, verbose_name="Title")
    text = models.TextField(verbose_name="Text")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
