from rest_framework import serializers
from responses.models import Response


class ResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    level = serializers.IntegerField()
    app_id = serializers.IntegerField()
    args = serializers.CharField(style={'base_template': 'textarea.html'})
    core = serializers.CharField(style={'base_template': 'textarea.html'})
    command = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Response.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.level = validated_data.get('level', instance.level)
        instance.app_id = validated_data.get('app_id', instance.app_id)
        instance.args = validated_data.get('args', instance.args)
        instance.core = validated_data.get('core', instance.core)
        instance.command = validated_data.get('command', instance.command)
        instance.save()
        return instance
