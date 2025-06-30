from django.urls import path
from .views import ActivosImportantesExcelAPIView, dashboard, health_check

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('api/activos-excel/', ActivosImportantesExcelAPIView.as_view(), name='activos-excel'),
    path('api/health/', health_check, name='health-check'),
] 