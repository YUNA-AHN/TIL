from rest_framework import serializers
from .models import DepositProducts, DepositOptions

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product',)

class DepositProductsSerializer(serializers.ModelSerializer):
    depositoptions_set = DepositOptionsSerializer(many=True, read_only=True)
    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = ('__all__')