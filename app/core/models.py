from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
from parametros.models import TipoDocu, EstaCivil, Etnia, TipoLogr, TipoEstu

# Importamos la lista de tipos de mensajes.
from .pqrsf import PQRSF_CHOICES

#create your models here
class Contact(models.Model):
	"""docstring for Contact"""
	email = models.EmailField(max_length = 50, verbose_name ="correo electrónico")
	tipom = models.CharField(max_length = 50, choises=PQRSF_CHOICES, default="peticion", verbose_name="categoria")
	nombre = models.CharField(max_length = 250, verbose_name = "nombre")
	msj = RichTextField(default="quisiera", verbose_name = "mensaje")

	#subclase para orgaizar los nombres de acuerdo al diccionario que usemos:
	class Meta:
		verbose_name = "Mensajes PQRSF"
		verbose_name_plural = "Mensajes PQRSF"

	def __str__(self):
		return self.nombre


class Usuarios(models.Model):
	IdUsuario = models.CharField(max_length = 50, verbose_name = "No. Identificación", default="")
	idTipoDocu = models.ForeignKey(TipoDocu, default="", on_delete=models.CASCADE, verbose_name="Tipo de documento")
	idEstaCivil = models.ForeignKey(EstaCivil, default="", on_delete=models.CASCADE, verbose_name="Estaco civil")
	idEtnias = models.ForeignKey(Etnia, default="", on_delete=models.CASCADE, verbose_name="Etnias")
	ImaUsua = models.ImageField(verbose_name = "Foto de perfil", upload_to = "perfiles/img")
	PerfiPro = RichTextField(default="Candidato...", verbose_name = "Perfil profecional")
	GeneUsua = models.CharField(max_length = 1, default="0", verbose_name="Genero")
	TeleUsua = models.CharField(max_length = 20, default="0", verbose_name="Telefono")
	CeluUsua = models.CharField(max_length = 20, default="0", verbose_name="Celular")
	DireUsua = models.TextField(default="0", verbose_name="Direccion postal")
	RegiUsua = models.DateTimeField(default=0, auto_now_add = False, verbose_name = "registrado el:")
	EstaUsua = models.CharField(max_length = 50, default="Activo", verbose_name = "Estado")

	class Meta:
		verbose_name = "Candidato"
		verbose_name_plural = "Candidatos"

	#ya creada la clase, retornamos el objeto NombEtni, o nombre de etnia:
	def __str__(self):
		return self.IdUsuario

class Experiencia(models.Model):
	#Atributos de la clase experiencia:
	CargExpe = models.ForeignKey(Empleos, on_delete=models.CASCADE, limit_choices_to={'Escargo': 'SI'}, verbose_name="Cargo Ocupado")
	EmprExpe = models.CharField(max_length = 150, verbose_name="Empresa")
	TeleEmpr = models.CharField(max_length = 30, verbose_name="Telefono de contacto de la empresa")
	JefeExpe = models.CharField(max_length = 30, verbose_name="Persona de contacto de la empresa")
	FechInic = models.DateTimeField(auto_now_add = False, default=0, verbose_name="Fecha de inicio")
	FachaFin = models.DateTimeField(auto_now_add = False, default=0, verbose_name="Fecha de terminacion")
	FuncionE = RichTextField(verbose_name="Funciones desempeñadas")
	LogrExpe = RichTextField(verbose_name="Logros alcanzados")
	SopoExpe = models.FileField(upload_to="soportes/laboral")
	EstaExpt = models.CharField(max_length=30, default="Activo", verbose_name="Estado de experiencia")

	class Meta:
		verbose_name = "Experiencia"
		verbose_name_plural = "Experiencia laboral"

	def __str__(self):
		return self.CargExpe

class Educacion(models.Model):

	TipoEstu = models.ForeignKey(TipoLogr, on_delete=models.CASCADE, default="", verbose_name="tipo de Educaciòn")
	Instituto = models.CharField(max_length= 30, default="Activo", verbose_name="Instituciòn o Academia")
	TituloEst = models.CharField(max_length=250, verbose_name="Titulo Obtenido")
	FechaGrado = models.DateTimeField(auto_now_add = False, default=0, verbose_name="Fecha de Graduacion")
	SoporteEs = models.FileField(upload_to="soportes/Educaciòn", default="", verbose_name="Soporte Educaciòn")
	EstaEstu = models.CharField(max_length= 30, default="Activo", verbose_name="Estado Educaciòn")

class Meta:

    verbose_name = "Educaciòn"
    verbose_name_plural = "Estudios Registrados"

def __str__(self):
	return self.TituloEst

# Clase para almacenar lo logros obtenidos
class logros(models.Model):
	NombTilo = models.ForeignKey(TipoLogr, on_delete=models.CASCADE, verbose_name="Tipo de Logro")
	FechLogr = models.DateTimeField(auto_now_add = False, default=0, verbose_name="Fecha de Culminacion de Logro")
	NombLogr = models.CharField(max_length= 100, default= "Activo", verbose_name = "Logro o Disticiòn")
	DescLogr = RichTextField(verbose_name="Descripciòn o Caracteristicas del Logro")

	class Meta:
		verbose_name = "Logros"
		verbose_name_plural = "Logros Obtenidos"

		def __str__(self):
			return self.NombLogr
# Clase para almacenar las habilidades del cadidato:

class Habilidades(models.Model):
	NombHabil = models.CharField(max_length= 100, default="Activo", verbose_name = "Habilidad")
	NiveHabil = models.CharField(max_length= 20, default="Activo", verbose_name = "Nivel de Habilidad:")

class Meta:
	verbose_name = "Habilidades"
	verbose_name = "Habilidades y Competencias"
	def __str__(self):
		return self.NombHabil















