from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from responses.models import Response
from responses.serializers import ResponseSerializer


@csrf_exempt
def response_list(request):
    if request.method == 'GET':
        responses = Response.objects.all()
        serializer = ResponseSerializer(responses, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ResponseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print('Response received')
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def response_detail(request, pk):
    try:
        response = Response.objects.get(pk=pk)
    except Response.DoesNotExist:
        return HttpResponse(status=404)

    if request.method  == 'GET':
        serializer = ResponseSerializer(response)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ResponseSerializer(response, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        response.delete()
        return HttpResponse(status=204)
