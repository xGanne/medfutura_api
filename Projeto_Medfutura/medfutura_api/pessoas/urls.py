from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PessoaViewSet

router = DefaultRouter()
router.register(r'pessoas', PessoaViewSet, basename='pessoa')

urlpatterns = [
    path('', include(router.urls)),
]