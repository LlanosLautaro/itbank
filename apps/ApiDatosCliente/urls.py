from django.urls import path
from .views import ClienteDetalles

urlpatterns = [
    path('<int:pk>/',ClienteDetalles.as_view({'get': 'retrieve'}))
]
