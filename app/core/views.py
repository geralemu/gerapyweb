from django.shortcuts import render, HttpResponse, redirect

from django.urls import reverse

from .forms import ContactForm


from django.shortcuts import render, get_object_or_404

from django.views.generic.base import TempleteView

from django.Views.generic.list import listView

from .models import  Usuarios, Experiencia, Logros, habilodades, Educacion

# Create your views here.Creamos nuestra vista de index:


def indexcore(request):
	#Instanciamos el formulario de contacto:
	FormContact = ContactForm()
	#validamos que se haya hecho la petcion POST del formulario de contacto
	if request.method = "POST":
		#Re asignamos el valor de FormContact, esta vez con todos los datos del formulario
		FormContact = ContactForm(data=request.POST)
		#validaremos que todos los campos sean del tipo de dato correcto:
		if FormContact.is_valid():
			#retornamos los valores de los campos:
			email = request.POST.get('email', '')
			tipom = request.POST.get('tipom', '')
			nombre = request.POST.get('nombre', '')
			msj = request.POST.get('msj', '')
			# si todo sale bien, guardamos y redireccionamos el nombre de la url con un mensaje:
			FormContact.save()
			return redirect(reverse('inicio')+"?Ok")
			#otra forma de redireccionar:
			#return redirect('/indexcore/?Ok!')
			#despues de instanciado lo pasamos en un diccionario de contexto:

	return render(request, 'core/index.html', {'formulario': FormContact})		









def indexcore(request):
	return render(request, 'core/index.html')


def nosotros(request):
	return render(request, 'core/nosotros.html')	


def base(request):
	return render(request, 'core/base.html')
	

