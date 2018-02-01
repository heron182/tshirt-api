from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from tshirt.models import Color, Category, Brand
from tshirt.serializers import ColorSerializer, CategorySerializer, BrandSerializer


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'colors':
            reverse(ColorList.name, request=request),
            'categories':
            reverse(CategoryList.name, request=request),
            'brands':
            reverse(BrandList.name, request=request)
        })


class ColorList(generics.ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    name = 'color-list'


class ColorListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    name = 'color-detail'


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-list'


class CategoryListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-detail'


class BrandList(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    name = 'brand-list'


class BrandListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    name = 'brand-detail'