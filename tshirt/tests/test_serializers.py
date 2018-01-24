import pytest

from tshirt.models import Tshirt
from tshirt.serializers import TshirtSerializer


@pytest.mark.django_db(transaction=True)
class TestTshirtSerializer:
    def test_can_serialize_tshirt_model(self):
        tshirt = Tshirt(
            brand='Volcom',
            quantity=10,
            size='M',
        )
        tshirt.save()
        serialized_tshirt = TshirtSerializer(tshirt)
        pk = serialized_tshirt.data['pk']
        assert tshirt == Tshirt.objects.get(pk=pk)

    def test_can_save_serialized_data_to_db(self):
        tshirt_data = {'brand': 'Volcom', 'size': 'M', 'quantity': 10}
        serialized_tshirt = TshirtSerializer(data=tshirt_data)
        assert serialized_tshirt.is_valid()
