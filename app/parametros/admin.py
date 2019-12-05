from django.contrib import admin

#importamos cada una de las clases creadas en el archivo models.py:
from .models import Etnia
from .models import TipoDocu
from .models import EstaCivil
from .models import TipoEstu
from .models import TipoLogr

# Register your models here.
#agregamos la clase <<model>>modeladmin, para modificar la vista a cada uno de los modelos importados

class EtniaModelAdmin(admin.ModelAdmin):
	#indicamos que columnas queremos ver, en este caso solo mostramos el nombre ya que no tenemos otras
	list_display = ["NombEtni"]
	#indicamos que columna, hacemos click para editar:
	#list_display_links = [NombEtni]
	#agregamos una barra de busqueda:
	search_fields = ["NombEtni"]
	#podemos aagregar un filtro:
	list_filter = ["NombEtni"]

	#indicamos desde donde se obtienen estos parametros:
	class Meta:
		model = Etnia

class TipoDocuModelAdmin(admin.ModelAdmin):
	list_display = ["NombTipo"]
	search_fields = ["NombTipo"]
	list_filter = ["NombTipo"]

	class Meta: 
		model = TipoDocu


class EstaCivilModelAdmin(admin.ModelAdmin):
	list_display = ["NomEsCi"]
	search_fields = ["NomEsCi"]
	list_filter = ["NomEsCi"]

	class Meta: 
		model = EstaCivil


class TipoEstuModelAdmin(admin.ModelAdmin):
	list_display = ["NombTiEs"]
	search_fields = ["NombTiEs"]
	list_filter = ["NombTiEs"]

	class Meta: 
		model = TipoEstu		



class TipoLogrModelAdmin(admin.ModelAdmin):
	list_display = ["NombTiLo"]
	search_fields = ["NombTiLo"]
	list_filter = ["NombTiLo"]

	class Meta: 
		model = TipoLogr	



admin.site.register(Etnia)
admin.site.register(TipoDocu)
admin.site.register(EstaCivil)
admin.site.register(TipoEstu)
admin.site.register(TipoLogr)