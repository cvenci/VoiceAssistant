from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from command.models import Command
from command.serializers import CommandSerializer


@csrf_exempt
def command_list(request):
    if request.method == 'GET':
        commands = Command.objects.all()
        serializer = CommandSerializer(commands, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CommandSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, srarus=400)


@csrf_exempt
def command_detail(request, pk):
    try:
        command = Command.objects.get(pk=pk)
    except Command.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = CommandSerializer(command)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CommandSerializer(command, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        command.delete()
        return HttpResponse(status=204)
