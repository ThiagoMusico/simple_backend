from django.urls import path
from .views import ListOportunidadesView


urlpatterns = [
    path('opts/', ListOportunidadesView.as_view(), name="oportunidades-all")
]