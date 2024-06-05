from django import forms

class seccion_dorada_formulario(forms.Form):
    field1 = forms.CharField(label='Intervalo', max_length=100, widget=forms.TextInput(attrs={'id': 'field1'}))
    field2 = forms.CharField(label='Funcion', max_length=100, widget=forms.TextInput(attrs={'id': 'field2'}))

class multiplicadores_formulario(forms.Form):
    field1 = forms.CharField(label='Funcion Objetivo', max_length=100, widget=forms.TextInput(attrs={'id': 'field1'}))
    field2 = forms.CharField(label='Restriccion', max_length=100, widget=forms.TextInput(attrs={'id': 'field2'}))
    
class GradienteFormulario(forms.Form):
    funcion_objetivo = forms.CharField(label='Función Objetivo', max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Ejemplo: 4*x1 + 6*x2 - 2*x1**2 - 2*x1*x2 - 2*x2**2'}))

class cuadratica_formulario(forms.Form):
    field1 = forms.CharField(label='Funcion Objetivo', max_length=100, widget=forms.TextInput(attrs={'id': 'field1'}))
    field2 = forms.CharField(label='Restriccion', max_length=100, widget=forms.TextInput(attrs={'id': 'field2'})) 
    
class combinaciones_formulario(forms.Form):
    field1 = forms.CharField(label='Funcion Objetivo', max_length=100, widget=forms.TextInput(attrs={'id': 'field1'}))
    field2 = forms.CharField(label='Restriccion', max_length=100, widget=forms.TextInput(attrs={'id': 'field2'})) 
    
class sumt_formulario(forms.Form):
    field1 = forms.CharField(label='Funcion Objetivo', max_length=100, widget=forms.TextInput(attrs={'id': 'field1'}))
    field2 = forms.CharField(label='Restriccion', max_length=100, widget=forms.TextInput(attrs={'id': 'field2'})) 
    
class separable_formulario(forms.Form):
    field1 = forms.CharField(label='Funcion Objetivo', max_length=100, widget=forms.TextInput(attrs={'id': 'field1'}))
    field2 = forms.CharField(label='Restriccion', max_length=100, widget=forms.TextInput(attrs={'id': 'field2'})) 