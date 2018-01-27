import pytest

from tshirt.models import Brand, Category, Color, Tshirt


@pytest.mark.django_db()
class TestColor:
    def test_can_save_a_color_in_db(self):
        color = Color(name='Blue')
        color.save()
        assert Color.objects.all().first() == color


@pytest.mark.django_db()
class TestCategory:
    def test_can_save_a_category_in_db(self):
        category = Category(name='Short Sleeve')
        category.save()
        assert Category.objects.all().first() == category


@pytest.mark.django_db()
class TestBrand:
    def test_can_save_a_brand_in_db(self):
        brand = Brand(name='Volcom')
        brand.save()
        assert Brand.objects.all().first() == brand


@pytest.mark.django_db()
class TestTshirt:
    def test_can_save_a_tshirt_in_db(self):
        color = Color(name='Blue')
        color.save()
        brand = Brand(name='Volcom')
        brand.save()
        category = Category(name='Short Sleeve')
        category.save()
        tshirt = Tshirt(
            name='Black city',
            color=color,
            brand=brand,
            category=category,
            size='L',
            quantity=10,
            unity_price=79.90)
        tshirt.save()
        assert Tshirt.objects.all().first() == tshirt
