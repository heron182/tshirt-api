from rest_framework import serializers
from tshirt.models import Tshirt


class TshirtSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=150)
    size = serializers.CharField(max_length=3)
    quantity = serializers.IntegerField()

    def create(self, validated_data):
        return Tshirt.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.brand = validated_data.get('brand', instance.name)
        instance.size = validated_data.get('size', instance.size)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance
