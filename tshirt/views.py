from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from tshirt.models import Tshirt
from tshirt.serializers import TshirtSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super().__init__(content, **kwargs)


@csrf_exempt
def tshirt_list(request):
    if request.method == 'GET':
        tshirts = Tshirt.objects.all()
        tshirts_serializer = TshirtSerializer(tshirts, many=True)
        return JSONResponse(tshirts_serializer.data)
    elif request.method == 'POST':
        tshirt_data = JSONParser().parse(request)
        tshirt_serializer = TshirtSerializer(data=tshirt_data)
        if tshirt_serializer.is_valid():
            tshirt_serializer.save()
            return JSONResponse(
                tshirt_serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(
            tshirt_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
