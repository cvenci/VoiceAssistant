from django.db import models

# This model represent the command sent by the user and the reponse to it 

class Command(models.Model):
    created  = models.DateTimeField(auto_now_add=True)
    core = models.TextField()

    class Meta:
        ordering = ['created']

