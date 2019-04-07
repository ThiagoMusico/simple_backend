from rest_framework import serializers
from .models import Oportunidades


class OportunidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oportunidades
        fields = ("titulo", "descricao", "local", "assunto", "tipo", "link", "data", "distancia")