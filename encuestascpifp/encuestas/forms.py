from django import forms
from .models import Pregunta, Usuario, Tipo_Pregunta, Opcion_Pregunta, User

class UsuarioForm(forms.ModelForm):
    
    class Meta:

        model = Usuario

        fields = [
            'user',
        ]

        widgets = {
            'user':forms.TextInput(attrs={'class':'form-control'})
        }

class PreguntaForm(forms.ModelForm):

    class Meta:
        model = Pregunta

        fields = [
            'pregunta',
            'tipo_pregunta',
        ]

        labels = {
            'pregunta':'Pregunta',
            'tipo_pregunta':'Tipo_Pregunta',
        }

        widgets = {
            'pregunta':forms.TextInput(attrs={'class':'form-control'}),
            'tipo_pregunta':forms.Select(attrs={'class':'form-control','required':'True'}),
        }