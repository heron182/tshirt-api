import json

import pytest
from django.test import Client

from tshirt.models import Tshirt
from tshirt.views import tshirt_list


@pytest.mark.django_db(transaction=True)
class TestTshirtCollection:
    def test_get_a_list_of_tshirts_as_json(self):
        Tshirt.objects.create(brand='Volcom', quantity=10, size='M')
        Tshirt.objects.create(brand='Zoo York', quantity=5, size='S')
        client = Client()
        resp = client.get('/tshirt/')
        assert resp.json() == [{
            'brand': 'Volcom',
            'pk': 1,
            'quantity': 10,
            'size': 'M'
        }, {
            'brand': 'Zoo York',
            'pk': 2,
            'quantity': 5,
            'size': 'S'
        }]
        assert resp.status_code == 200

    def test_post_a_new_tshirt(self):
        post_data = {"brand": "Volcom", "quantity": 10, "size": "M"}
        client = Client()
        resp = client.post(
            '/tshirt/',
            data=json.dumps(post_data),
            content_type='application/json')
        assert len(
            Tshirt.objects.filter(brand="Volcom", quantity=10, size="M")) == 1
        assert resp.status_code == 201
