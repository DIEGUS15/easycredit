from rest_framework import serializers  # , viewsets
from .models import ProductType, Provider, Product


# Serializer for ProductType
class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'  # ['name', 'status']

# Serializer for Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'  # ['name', 'status']

# Serializer for Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.SlugRelatedField(
    #     queryset=User.objects.all(), slug_field='username')
    type = serializers.SlugRelatedField(
        queryset=ProductType.objects.all(), slug_field='name')
    provider = serializers.SlugRelatedField(
        queryset=Provider.objects.all(), slug_field='name')

    class Meta:
        model = Product
        # ['reference', 'type', 'provider', 'name', 'value', 'stock', 'status', 'description']
        fields = '__all__'

    # def create(self, validated_data):
    #     validated_data['user'] = self.context['request'].user
    #     return super(ProductSerializer, self).create(validated_data)
