from django.db import models


class Oportunidades(models.Model):
	# Opt titulo
	titulo = models.CharField(max_length=255, null=False)
	# Opt descricao
	descricao = models.TextField()
	# Opt local
	local = models.CharField(max_length=255, null=False)
	# Opt assunto
	assunto = models.CharField(max_length=255, null=False)
	# Opt tipo
	tipo = models.CharField(max_length=255, null=False)
	# Opt link
	link = models.CharField(max_length=255, null=False)
	# Opt data
	data = models.CharField(max_length=255, null=False)
	# Opt distancia
	distancia = models.CharField(max_length=255, null=False)

	def __str__(self):
		return "{} - {}".format(self.titulo, self.tipo)


# Create your models here.
