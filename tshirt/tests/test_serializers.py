import pytest

from tshirt.models import Tshirt
from tshirt.serializers import TshirtSerializer


@pytest.mark.django_db(transaction=True)
class TestTshirtSerializer:
    def test_can_serialize_tshirt_model(self):
        tshirt = Tshirt(brand='Volcom', quantity=10, size='M')
        tshirt.save()
        serialized_tshirt = TshirtSerializer(tshirt)
        assert serialized_tshirt.data == {
            'pk': 1,
            'brand': 'Volcom',
            'size': 'M',
            'quantity': 10
        }

    def test_can_save_serialized_data_to_db(self):
        tshirt_data = {'pk': 1, 'brand': 'Volcom', 'size': 'M', 'quantity': 10}
        serialized_tshirt = TshirtSerializer(data=tshirt_data)
        if serialized_tshirt.is_valid():
            tshirt = serialized_tshirt.save()
            assert isinstance(tshirt, Tshirt)
