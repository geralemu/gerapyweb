#importamos la libreria forms:
from django import forms

#creamos una lista de las posibles opciones del select:
from .pqrsf import PQRSF_CHOICES 

#creamos la estructura dl formulario
class ContactFrom(forms.Form):
	"""creamos los campos"""
email = forms.EmailField(label="correo electrónico", widget=forms.EmailInput(attrs={'class':'form-control'}), required=True)
tipom = forms.ChoiseField(choices = PQRSF_CHOICES, label="Tipo de atencion requerida", initial='', widget=forms.Select(attrs={'class':'form-control'}), required=True)
nombre = forms.CharField(label="nombre", required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
msj = forms.CharField(label="Mensaje", widget=forms.Textarea(attrs={'class':'form-control', 'rows':'3'}), required=True)