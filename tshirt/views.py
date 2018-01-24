from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from tshirt.models import Tshirt
from tshirt.serializers import TshirtSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
def tshirt_list(request):
    if request.method == 'GET':
        tshirts = Tshirt.objects.all()
        tshirts_serializer = TshirtSerializer(tshirts, many=True)
        return Response(tshirts_serializer.data)
    elif request.method == 'POST':
        tshirt_serializer = TshirtSerializer(data=request.data)
        if tshirt_serializer.is_valid():
            tshirt_serializer.save()
            return Response(
                data=tshirt_serializer.data, status=status.HTTP_201_CREATED)
    return Response(
        data=tshirt_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def tshirt_detail(request, pk):
    try:
        tshirt = Tshirt.objects.get(pk=pk)
    except Tshirt.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tshirt_serializer = TshirtSerializer(tshirt)
        return Response(data=tshirt_serializer.data)
    elif request.method == 'PUT':
        tshirt_serializer = TshirtSerializer(tshirt, data=request.data)
        if tshirt_serializer.is_valid():
            tshirt_serializer.save()
            return Response(data=tshirt_serializer.data)
        return Response(
            tshirt_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        tshirt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
