from django.shortcuts import render
from rest_framework import generics
from applications.products.models import Product, ProductImage
# from applications.feedback.models import Like, Rating
from applications.products.serializer import ProductSerializer, ProductImageSerializers
# from applications.feedback.serializers import RatingSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# from applications.products.permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action


class CustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsOwner]

    pagination_class = CustomPagination

    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['owner', 'title']
    # search_fields = ['title']
    # ordering_fields = ['id', 'owner']

    def perform_create(self, serializer):
        print(self.request.user, '!!!!')
        # serializer.save(owner=self.request.user)    
        # return serializer
        serializer.save(owner=self.request.user)


class CreateImageAPIView(generics.CreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


