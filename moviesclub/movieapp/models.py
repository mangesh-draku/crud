
from django.db import models

class movies (models.Model):
    name = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    summary = models.TextField(blank=True, null=True)

