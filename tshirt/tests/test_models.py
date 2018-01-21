import pytest
from django.test import TestCase

from tshirt.models import Tshirt


@pytest.mark.django_db(transaction=True)
class TestTshirt(TestCase):
    def test_tshirt_model_is_saved_to_db(self):
        tshirt = Tshirt(brand='Volcom', quantity=10, size='M')
        tshirt.save()
        self.assertEqual(len(Tshirt.objects.all()), 1)
