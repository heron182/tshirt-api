import json

import pytest
from django.test import Client

from tshirt.models import Tshirt
from tshirt.views import tshirt_list


@pytest.mark.django_db(transaction=True)
class TestTshirtCollection:
    def test_get_a_list_of_tshirts_as_json(self):
        Tshirt.objects.create(brand='Volcom', quantity=10, size='L', pk=1)
        Tshirt.objects.create(brand='Zoo York', quantity=5, size='S', pk=2)
        client = Client()
        resp = client.get('/tshirt/')
        assert resp.json() == [{
            'brand': 'Volcom',
            'pk': 1,
            'quantity': 10,
            'size': 'L'
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
        resp = client.post('/tshirt/', data=post_data)
        assert len(Tshirt.objects.filter(brand="Volcom", quantity=10)) == 1
        assert resp.status_code == 201

    def test_get_details_from_a_tshirt(self):
        Tshirt.objects.create(brand='Volcom', quantity=10, size='L', pk=1)
        client = Client()
        resp = client.get('/tshirt/1/')
        assert resp.json() == {
            'pk': 1,
            'brand': 'Volcom',
            'size': 'L',
            'quantity': 10
        }
        assert resp.status_code == 200

    def test_update_details_from_a_tshirt(self):
        Tshirt.objects.create(brand='Volcom', quantity=10, size='L', pk=1)
        put_data = {"brand": "Volcom", "quantity": 5, "size": "XL", "pk": 1}
        client = Client()
        resp = client.put(
            '/tshirt/1/',
            data=json.dumps(put_data),
            content_type='application/json')
        assert resp.json() == {
            'pk': 1,
            'brand': 'Volcom',
            'size': 'XL',
            'quantity': 5
        }
        assert resp.status_code == 200

    def test_delete_tshirt(self):
        Tshirt.objects.create(brand='Volcom', quantity=10, size='L', pk=1)
        client = Client()
        resp = client.delete('/tshirt/1/')
        assert resp.status_code == 204
