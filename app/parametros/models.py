from django.db import models

# Create your models here.
#los modelos son una clse que devuelve un objeto
#por lo que crearemos una clase con el nombre de la entidad o colección  y definiremos los atributos:

class Etnia(models.Model):
	NombEtni = models.CharField(max_length = 50)

	#ya creada la clase, retornamos el objeto NomEtni o nombre etnia:
	def __unicode__(self):
		return self.NomEtni

	   


	#agregamos las otrasc clases del modulo:

	#clase para el modelo tipo docu:
class TipoDocu(models.Model):
		NombTipo = models.CharField(max_length = 50)

		def __unicode__(self):
			return self.NombTipo
		

   #clase para el modelo estado civil:
class EstaCivil(models.Model):
	NomEsCi = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.NomEsCi
	

#clase para el modelo clasificacion de los estudios

class TipoEstu(models.Model):
	NombTiEs = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.NombTiEs
    


#clase para el modelo tipos de logro:

class TipoLogr(models.Model):
	NombTiLo = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.NombTiLo
	


