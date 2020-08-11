from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from commands.models import Commands
from commands.serializers import CommandsSerializer


@csrf_exempt
def commands_list(request):
    if request.method == 'GET':
        cmds = Commands.objects.all()
        serializer = CommandsSerializer(cmds, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CommandsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def commands_detail(request, pk):
    try:
        cmd = Commands.objects.get(pk=pk)
    except Commands.DoesNotExist:
        return HttpResponse(srarus=404)
    
    if request.method == 'GET':
        serializer = CommandsSerializer(cmd)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CommandsSerializer(cmd, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=404)
    
    elif request.method =='DELETE':
        cmd.delete()
        return HttpResponse(status=204)
        
