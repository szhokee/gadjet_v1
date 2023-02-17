from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('swagger/', schema_view.with_ui('swagger')),
    path('api/v1/account/', include('applications.account.urls')),
    path('api/v1/product/', include('applications.products.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
