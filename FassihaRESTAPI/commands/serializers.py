from rest_framework import serializers
from commands.models import Commands


class CommandsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    core = serializers.CharField(style={'base_template':'textarea.html'})

    def create(self, validated_data):
        return Commands.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.core = validated_data.get('core', instance.core)
        instance.save()
        return instance
