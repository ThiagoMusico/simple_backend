from django.shortcuts import render
from rest_framework import generics
from .models import Oportunidades
from .serializer import OportunidadesSerializer


class ListOportunidadesView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Oportunidades.objects.all()
    serializer_class = OportunidadesSerializer
# Create your views here.
