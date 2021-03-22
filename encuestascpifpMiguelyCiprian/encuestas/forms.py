from django import forms
from .models import Pregunta, Usuario, Tipo_Pregunta, Opcion_Pregunta, User, Encuesta_Pregunta

class UserForm(forms.ModelForm):
    
    class Meta:

        model = Usuario

        fields = [
            'user',
            'password'
        ]

        widgets = {
            'user':forms.TextInput(attrs={'class':'form-control','autocomplete':'Nombre del usuario', 'required':'True'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','autocomplete':'Añadir contraseña', 'required':'True'})
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
            'pregunta':forms.TextInput(attrs={'class':'form-control','required':'True'}),
            'tipo_pregunta':forms.Select(attrs={'class':'form-control','required':'True'}),
        }

class EncuestaForm(forms.ModelForm):

    class Meta:
        model = Encuesta_Pregunta

        fields = [
            'clave_acceso',
            'nombre',
        ]

        labels = {
            'clave_acceso':'Clave acceso',
            'nombre':'Nombre',
        }

        widgets = {
            'clave_acceso':forms.TextInput(attrs={'class':'form-control','required':'True'}),
            'nombre':forms.TextInput(attrs={'class':'form-control','required':'True'}),
        }
class UsuarioForm(forms.ModelForm):

    class Meta:

        model = Usuario

        fields = [
            'nombre_completo',
        ]
        labels = {
            'nombre_completo':'Usuario',
        }
        widgets = {
            'nombre_completo':forms.TextInput(attrs={'class':'form-control','required':'True'})
        }

class OpcionPreguntaTextForm(forms.ModelForm):
 
    class Meta:

        model = Opcion_Pregunta

        fields = [
            'opcion',
        ]
        labels={
            'opcion':'Opcion_Pregunta',
        }
        widgets = {
            'opcion':forms.TextInput(attrs={'class':'form-control'})
        }
