from django.db import models


class Commands(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    core = models.TextField()

    class Meta:
        ordering = ['created']