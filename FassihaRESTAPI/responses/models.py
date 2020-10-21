from django.db import models


class Response(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    level = models.IntegerField(default=2)
    app_id = models.IntegerField()
    args = models.TextField()
    core = models.TextField()
    command = models.TextField(default='')

    class Meta:
        ordering = ['created']
