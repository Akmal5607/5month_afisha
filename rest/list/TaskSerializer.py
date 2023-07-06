from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Nano


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nano
        fields = '__all__'


class TaskValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=5, max_length=100)
    description = serializers.CharField(required=False)
    price = serializers.FloatField(min_value=0, max_value=10000000)
    is_hit = serializers.BooleanField()
    category_id = serializers.IntegerField()




