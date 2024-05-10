from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.vendor_dashboard, name='dashboard'),
    path('api/vendor_clients/', views.vendor_clients, name='vendor_clients')
]