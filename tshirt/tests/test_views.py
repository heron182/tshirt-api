import json

import pytest
from django.test import Client

from tshirt.models import Tshirt
from tshirt.views import tshirt_list


@pytest.mark.django_db(transaction=True)
class TestTshirtCollection:
    client = Client()

    def test_get_a_list_of_tshirts_as_json(self):
        Tshirt.objects.create(brand='Volcom', quantity=10, size='L')
        Tshirt.objects.create(brand='Zoo York', quantity=5, size='S')
        resp = self.client.get('/tshirt/')
        assert len(resp.json()) == len(Tshirt.objects.all())
        assert resp.status_code == 200

    def test_post_a_new_tshirt(self):
        post_data = {"brand": "Volcom", "quantity": 10, "size": "M"}
        resp = self.client.post('/tshirt/', data=post_data)
        assert len(Tshirt.objects.all()) == 1
        assert resp.status_code == 201

    def test_get_details_from_a_tshirt(self):
        tshirt = Tshirt(brand='Volcom', quantity=10, size='L')
        tshirt.save()
        resp = self.client.get(f'/tshirt/{tshirt.pk}/')
        brand = resp.json()['brand']
        assert Tshirt.objects.get(brand=brand)
        assert resp.status_code == 200

    def test_update_details_from_a_tshirt(self):
        tshirt = Tshirt(brand='Volcom', quantity=10, size='L')
        tshirt.save()
        put_data = {"brand": "Volcom", "quantity": 5, "size": "XL"}
        resp = self.client.put(
            f'/tshirt/{tshirt.pk}/',
            data=json.dumps(put_data),
            content_type='application/json')
        size = resp.json()['size']
        assert tshirt == Tshirt.objects.get(size=size)
        assert resp.status_code == 200

    def test_delete_tshirt(self):
        tshirt = Tshirt(brand='Volcom', quantity=10, size='L')
        tshirt.save()
        resp = self.client.delete(f'/tshirt/{tshirt.pk}/')
        assert resp.status_code == 204
