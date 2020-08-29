from django.db import models


class Response(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    app_id = models.IntegerField()
    args = models.TextField()
    core = models.TextField()

    class Meta:
        ordering = ['created']
