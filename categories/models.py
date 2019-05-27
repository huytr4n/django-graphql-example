from django.db import models


class Category(models.Model):
    """
    Category model.
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at",
        blank=True,
        null=True
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated at",
        blank=True,
        null=True
    )
    name = models.CharField(max_length=255, verbose_name="Title")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title
