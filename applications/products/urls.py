from django.urls import path, include
from applications.products.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('comment', CommentModelViewSet)
router.register('', ProductModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add/image/', CreateImageAPIView.as_view()),
]