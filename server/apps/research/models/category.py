from django.db import models
from apps.common.models import BaseModel

class Category(BaseModel):
    """Model for categories."""
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
