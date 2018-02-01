from datetime import datetime

import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory

from tshirt.models import Brand, Category, Color, Tshirt
from tshirt.serializers import (BrandSerializer, CategorySerializer,
                                ColorSerializer, TshirtSerializer)
from tshirt.views import BrandListDetail, CategoryListDetail, ColorListDetail


@pytest.mark.django_db()
class BaseTestSerializer:
    request_factory = APIRequestFactory()

    @staticmethod
    def model_fields_in_serialized_data(model_as_dict, payload):
        return all(k in payload.keys() for k in model_as_dict.keys())


class TestColorSerializer(BaseTestSerializer):
    def test_can_create_color(self):
        color = {'name': 'blue'}
        serialized_color = ColorSerializer(data=color)
        serialized_color.is_valid()
        serialized_color.save()
        assert Color.objects.get(name='blue')

    def test_invalid_color_payload(self):
        color = {'name': None}
        serialized_color = ColorSerializer(data=color)
        assert serialized_color.is_valid() is False

    def test_can_serialize_a_color_from_db(self):
        color = Color(name='blue')
        color.save()
        request = self.request_factory.get(
            path=reverse(ColorListDetail.name, args=[color.pk]))
        serialized_color = ColorSerializer(color, context={'request': request})
        color_as_dict = Color.objects.filter(name='blue').values().first()
        assert self.model_fields_in_serialized_data(color_as_dict,
                                                    serialized_color.data)


class TestCategorySerializer(BaseTestSerializer):
    def test_can_create_category(self):
        category = {'name': 'Full sleeve'}
        serialized_category = CategorySerializer(data=category)
        serialized_category.is_valid()
        serialized_category.save()
        assert Category.objects.get(name='Full sleeve')

    def test_invalid_category_payload(self):
        category = {'name': None}
        serialized_category = CategorySerializer(data=category)
        assert serialized_category.is_valid() is False

    def test_can_serialize_a_category_from_db(self):
        category = Category(name='Full sleeve')
        category.save()
        request = self.request_factory.get(
            path=reverse(CategoryListDetail.name, args=[category.pk]))
        serialized_category = CategorySerializer(
            category, context={
                'request': request
            })
        category_as_dict = Category.objects.filter(
            name='Full sleeve').values().first()
        assert self.model_fields_in_serialized_data(category_as_dict,
                                                    serialized_category.data)


class TestBrandSerializer(BaseTestSerializer):
    def test_can_create_brand(self):
        brand = {'name': 'Volcom'}
        serialized_brand = BrandSerializer(data=brand)
        serialized_brand.is_valid()
        serialized_brand.save()
        assert Brand.objects.get(name='Volcom')

    def test_invalid_brand_payload(self):
        brand = {'name': None}
        serialized_brand = BrandSerializer(data=brand)
        assert serialized_brand.is_valid() is False

    def test_can_serialize_a_brand_from_db(self):
        brand = Brand(name='Volcom')
        brand.save()
        request = self.request_factory.get(
            path=reverse(BrandListDetail.name, args=[brand.pk]))
        serialized_brand = BrandSerializer(brand, context={'request': request})
        brand_as_dict = Brand.objects.filter(name='Volcom').values().first()
        assert self.model_fields_in_serialized_data(brand_as_dict,
                                                    serialized_brand.data)


class TestTshirtSerializer(BaseTestSerializer):
    @staticmethod
    def create_tshirt():
        color = Color(name='Blue')
        color.save()
        brand = Brand(name='Volcom')
        brand.save()
        category = Category(name='Short Sleeve')
        category.save()
        # tshirt = Tshirt(
        #     name='Black city',
        #     color=color,
        #     brand=brand,
        #     category=category,
        #     size='L',
        #     quantity=10,
        #     unity_price=79.90)
        # tshirt.save()

        return {
            'name': 'Black city',
            'brand': 'Volcom',
            'category': 'Short Sleeve',
            'color': 'Blue',
            'size': 'L',
            'quantity': 10,
            'unity_price': 79.90,
            'date_added': str(datetime.now())
        }

    def test_can_create_tshirt(self):
        tshirt = self.create_tshirt()
        serialized_tshirt = TshirtSerializer(data=tshirt)
        serialized_tshirt.is_valid()
        import pdb
        pdb.set_trace()
        serialized_tshirt.save()
        assert Tshirt.objects.get(name='Black city')

    def test_invalid_brand_payload(self):
        brand = {'name': None}
        serialized_brand = BrandSerializer(data=brand)
        assert serialized_brand.is_valid() is False

    def test_can_serialize_a_brand_from_db(self):
        brand = Brand(name='Volcom')
        brand.save()
        request = self.request_factory.get(
            path=reverse(BrandListDetail.name, args=[brand.pk]))
        serialized_brand = BrandSerializer(brand, context={'request': request})
        brand_as_dict = Brand.objects.filter(name='Volcom').values().first()
        assert self.model_fields_in_serialized_data(brand_as_dict,
                                                    serialized_brand.data)
