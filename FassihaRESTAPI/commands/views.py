from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from commands.models import Commands
from commands.serializers import CommandsSerializer

from responses.models import Response
from responses.serializers import ResponseSerializer
from rest_framework.renderers import JSONRenderer

from start import run


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
            # serializer.save()
            # HERE THE WORK #
            # print(data['core'])

            response_run = run(data['core'])
            print(response_run)
            response = Response.objects.get(pk=1)
            response.level = response_run['level']
            response.core = response_run['core']
            response.app_id = response_run['app_id']
            response.args = response_run['args']
            response.command = response_run['command']
            response.save()
            response_serializer = ResponseSerializer(response)
            content = JSONRenderer().render(response_serializer.data)
            # END  # 
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def commands_detail(request, pk):
    try:
        cmd = Commands.objects.get(pk=pk)
    except Commands.DoesNotExist:
        return HttpResponse(status=404)

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

    elif request.method == 'DELETE':
        cmd.delete()
        print('object deleted !!')
        return HttpResponse(status=204)
