from django import forms
class FormularioContacto(forms.Form):
    asunto= forms.CharField()
    email=forms.EmailField()
    mensaje= forms.CharField()
class FormularioActa(forms.Form):
    seccion=forms.CharField(label='BUSQUEDA POR SECCION', max_length=4)