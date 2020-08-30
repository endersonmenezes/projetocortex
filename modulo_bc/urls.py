from django.urls import path
from .views import converter_moedas

urlpatterns = [
    path('', converter_moedas),
]
