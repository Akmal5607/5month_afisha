from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Product, Category, Tag, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = 'id title price category tags category_name tags_name reviews'.split()
        # fields = '__all__'


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=5, max_length=100)
    description = serializers.CharField(required=False)
    price = serializers.FloatField(min_value=0, max_value=10000000)
    is_hit = serializers.BooleanField()
    category_id = serializers.IntegerField()
    tags = serializers.ListField(child=serializers.IntegerField(min_value=1))

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category not found!')
        return category_id

    def validate_tags(self, tags):
        tags_obj = Tag.objects.filter(id__in=tags)
        if len(tags) != len(tags_obj):
            raise ValidationError('Tag not found!')
        return tags
