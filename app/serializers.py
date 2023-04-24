from rest_framework import serializers

from .models import Category,Product


class ProductSerializer(serializers.Serializer):
    name=serializers.CharField()
    price=serializers.IntegerField()
    category_id=serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(
            name=validated_data['name'],
            price=validated_data['price'],
            category_id=validated_data['category_id']
        )

    def update(self, instance, validated_data):
        pass


class CategorySerializer(serializers.Serializer):
    name=serializers.CharField()

    def create(self, validated_data):
        return Category.objects.create(name=validated_data['name'])

    def update(self, instance, validated_data):
        pass