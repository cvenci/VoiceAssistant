from rest_framework import serializers
from command.models import Command


class CommandSerializer(serializers.Serializer):
    class Meta:
        model = Command
        fields = ['id', 'core']
