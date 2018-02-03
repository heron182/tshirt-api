from rest_framework import serializers

from tshirt.models import Brand, Category, Color, Tshirt


class ColorSerializer(serializers.HyperlinkedModelSerializer):
    tshirts = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='color-detail')

    class Meta:
        model = Color
        fields = ('url', 'id', 'name', 'tshirts')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    tshirts = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='category-detail')

    class Meta:
        model = Category
        fields = ('url', 'id', 'name', 'tshirts')


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    tshirts = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='brand-detail')

    class Meta:
        model = Brand
        fields = ('url', 'id', 'name', 'tshirts')


class TshirtSerializer(serializers.HyperlinkedModelSerializer):
    brand = serializers.SlugRelatedField(
        queryset=Brand.objects.all(), slug_field='name')
    color = serializers.SlugRelatedField(
        queryset=Color.objects.all(), slug_field='name')
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field='name')

    class Meta:
        model = Tshirt
        fields = ('url', 'id', 'name', 'brand', 'category', 'color',
                  'quantity', 'unity_price', 'size')
