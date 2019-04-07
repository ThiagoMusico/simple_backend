from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Oportunidades
from .serializer import OportunidadesSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_opt(titulo="", descricao="", local="", assunto="", tipo="", link="", data="", distancia=""):
        if titulo != "" and descricao != "" and local != "" and assunto != "" and tipo != "" and link != "" and data != "" and dist != "":
            Oportunidades.objects.create(titulo=titulo, descricao=descricao, local=local, assunto=assunto, tipo=tipo, link=link, data=data, distancia=dist)


    def setUp(self):
        # add test data
        self.create_opt("Palestra do Monaco", "Só batatisse nessa palestra", "ICMC", "tech", "palestra", "n tem", "07/04/2019", "1 km")
        self.create_opt("IC em razer", "Venha fazer ic em jogo de ricos", "lasejdgoiasijdg", "jogos", "ic", "laljshga", "10/07/2019", "3 km")
        self.create_opt("Estagio na Klabin", "Só klabins serão aceitos até o fim de 2040.", "Klabin", "estagio", "estagio", "asdgasdgsag", "03/06/2020", "200 m")



class GetAllOportunidadesTest(BaseViewTest):

    def test_get_all_opts(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the opts/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("oportunidades-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Oportunidades.objects.all()
        serialized = OportunidadesSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Create your tests here.
