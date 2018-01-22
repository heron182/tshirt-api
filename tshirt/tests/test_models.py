import pytest

from tshirt.models import Tshirt


@pytest.mark.django_db(transaction=True)
class TestTshirt:
    def test_tshirt_model_is_saved_to_db(self):
        tshirt = Tshirt(brand='Volcom', quantity=10, size='M')
        tshirt.save()
        assert len(Tshirt.objects.all()) == 1
