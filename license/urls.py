

from django.urls import path
from .views import LicenseDetailView, LicenseActivationView, APIHome
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="License API",
        default_version='v1',
        description="API for managing licenses",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="haradhan.sharma@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

app_name = 'license'
urlpatterns = [
    path('license/<str:license_key>/', LicenseDetailView.as_view(), name='license-detail'),
    path('license/activate/<str:license_key>/', LicenseActivationView.as_view(), name='license-activate'),    
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('lmapi<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),      
    path('lmapi.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

