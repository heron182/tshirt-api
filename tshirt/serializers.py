from rest_framework import serializers

from tshirt.models import Tshirt


class TshirtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tshirt
        fields = ('pk', 'brand', 'quantity', 'size', 'date_added')
