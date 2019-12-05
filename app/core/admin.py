from django.contrib import admin

# Register your models here.

class UsuariosModelAdmin(admin.ModelAdmin):
	#indicamos que columnas queremos ver:
    list_display = ("__srt__", "IdUsuario", "ImagUsua", "EstaUsua")
    #Agregamos una barra de busqueda:
    search_fields = ('IdUsuario', 'GeneUsua', 'CeluUsua', 'TeleUsua',)
    #podemos agregar un filtro:
    list_filter = ('IdUsuario', 'GeneUsua',)
    #mostramos las fechas de creacion del usuario:
    readonly_fields = ('RegiUsua',)
    #Indicamos desde donde se obtienen estos parametros:
    class Meta:
	    model = Usuarios 
    admin.site.register(Usuarios, UsuariosModelAdmin)	

class ExperienciaModelAdmin(admin.ModelAdmin):
	#indicamos que columnas queremos ver:
	list_display = ("__srt__", "CargExpe", "EmprExpe", "FechInic", "FechaFin", "SopoExpe")
    #Agregamos una barra de busqueda:	
    search_fields = ('CargExpe', 'EmprExpe',)
    #podemos agregar un filtro:
    list_filter = ('CargExpe', 'FechaFin',)
    #mostramos las fechas de creacion del usuario:
    readonly_fields = ('EstaExpt',)
    #Indicamos desde donde se obtienen estos parametros:
    class Meta:
	    model = Experiencia
    admin.site.register(Experiencia, ExperienciaModelAdmin)

class EducacionModeloAdmin(admin.ModelAdmin):

	list_display = ("__str__", "TipoEstu", "TituloEst", "FechGrado", "Instituto", "SoporteEs")
	# Agregamos una barra de busqueda:
	search_fields = ('TituloEst','TipoEstu',)
	# Podemos agregar un filtro:
	list_filter = ('TipoEstu','FechGrado',)
	# Mostramos las fechas de creacion de usuario:
	readonly_fields = ('EstaEstu',)
	#Indicamos desde donde se obtienen estos parametros:
	class Meta:
		 model = Educacion
	admin.site.register(Educacion, ExperienciaModelAdmin)

class LogrosModelAdmin(admin.ModelAdmin):
    # Indicamos que columnas queremos ver :
	list_display = ("__str__", "NombLogr", "FechLogr", "NombTiLo")
	# Agregamos una barra de busqueda:
	search_fields = ('NombLogr', 'NombTiLo', 'FechLogr',)
	# Podemos agregar un filtro:
	list_filter = ('NombTiLo','FechLogr','NombLogr',)
	# Mostramos las fechas de creacion del usuario:
	# Readoly_fields = ('EstaEstu')
	# Indicamos desde donde se obtienen estos parametros:
	class Meta:
		model = Logros
	Admin.site.register(Logros, LogrosModelAdmin)


class HabilidadesModelAdmin(admin.ModelAdmin):
    # Indicamos que columnas queremos ver :	
    list_display = ("__str__", "NombHabil", "NiveHabil")
    # Agregamos una barra de busqueda:
	search_fields = ('NombHabil', 'NiveHabil',)
	# Podemos agregar un filtro:
	list_filter = ('NiveHabil', 'NombHabil',)
	# Mostramos las fechas de creacion del usuario:
	# Readoly_fields = ('EstaEstu')
	# Indicamos desde donde se obtienen estos parametros:
	class Meta:
		model = Habilidades 
	admin.site.register(Habilidades, HabilidadesModelAdmin)	






