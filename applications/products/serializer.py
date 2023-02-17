from rest_framework import serializers
from applications.products.models import Product, ProductImage
# from applications.feedback.serializers import LikeSerializer
from django.db.models import Avg


class ProductImageSerializers(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = '__all__'


# class ProductSerializer(serializers.ModelSerializer):
#     images = ProductImageSerializers(many=True, read_only=True)
#     # likes = LikeSerializer(many=True, read_only= True)
#     # owner = serializers.ReadOnlyField(source='owner.email')

#     class Meta:
#         model = Product
#         fields = '__all__'