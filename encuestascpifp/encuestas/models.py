from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Tipo_Pregunta(models.Model):
    tipo = models.CharField(max_length=45)
    class Meta:
        ordering = ['tipo']
    
    def __str__(self):
        return '{}'.format(self.tipo)

class Pregunta(models.Model):
    pregunta = models.CharField(max_length=100)
    tipo_pregunta = models.ForeignKey(Tipo_Pregunta, on_delete=models.CASCADE)
    class Meta:
        ordering = ['pregunta']

    def __str__(self):
        return '{}'.format(self.pregunta)

class Opcion_Pregunta(models.Model):
    opcion = models.CharField(max_length=100)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    class Meta:
        ordering = ['opcion']
    def __str__(self):
        return '{}'.format(self.opcion)

class Departamento(models.Model):
    departamento = models.CharField(max_length=100)
    departamento_corto = models.CharField(max_length=10)
    class Meta:
        ordering = ['departamento']
    def __str__(self):
        return'{}'.format(self.departamento)

class Rol(models.Model):
    rol = models.CharField(max_length=45)
    class Meta:
        ordering = ['rol']
    def __str__(self):
        return'{}'.format(self.rol)

class Evaluacion(models.Model):
    evaluacion = models.CharField(max_length=45)
    class Meta:
        ordering = ['evaluacion']
    def __str__(self):
        return'{}'.format(self.evaluacion)

class Tipo_Pregunta_Encuesta(models.Model):
    tipo_pregunta_encuesta = models.CharField(max_length=45)
    class Meta:
        ordering = ['tipo_pregunta_encuesta']
    
    def __str__(self):
        return '{}'.format(self.tipo_pregunta_encuesta)

class Anio_lectivo(models.Model):
    anio_lectivo = models.CharField(max_length=45)
    class Meta:
        ordering = ['anio_lectivo']

    def __str__(self):
        return '{}'.format(self.anio_lectivo)
        
class Ciclo(models.Model):
    ciclo = models.CharField(max_length=100)
    ciclo_corto = models.CharField(max_length=45)
    class Meta:
        ordering = ['ciclo']

    def __str__(self):
        return '{}'.format(self.ciclo)

class Curso(models.Model):
    curso = models.CharField(max_length=45)
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    class Meta:
        ordering = ['curso']

    def __str__(self):
        return '{}'.format(self.curso)

class Modulo(models.Model):
    modulo = models.CharField(max_length=100)
    nombre_corto = models.CharField(max_length=10)
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    class Meta:
            ordering = ['modulo']
    def __str__(self):
        return '{}'.format(self.modulo)

#ORDERING Y STR revisar
class Encuesta(models.Model):
    clave_acceso = models.CharField(max_length=45)
    estado = models.IntegerField()
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    anio_lectivo = models.ForeignKey(Anio_lectivo, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    class Meta:
        ordering = ['clave_acceso']

    def __str__(self):
        return '{}'.format(self.clave_acceso)

class Pregunta_Encuesta(models.Model):
    pregunta_encuesta = models.CharField(max_length=100)
    tipo_pregunta_encuesta = models.ForeignKey(Tipo_Pregunta_Encuesta, on_delete=models.CASCADE)
    class Meta:
        ordering = ['pregunta_encuesta']

    def __str__(self):
        return '{}'.format(self.pregunta_encuesta)

class Opcion_Pregunta_Encuesta(models.Model):
    opcion_pregunta_encuesta = models.CharField(max_length=100)
    pregunta_encuesta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    class Meta:
        ordering = ['opcion_pregunta_encuesta']
    def __str__(self):
        return '{}'.format(self.opcion_pregunta_encuesta)

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    nombre_completo = models.CharField(max_length=100)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    class Meta:
        ordering = ['user']
    def __str__(self):
        return '{}'.format(self.user)

class Usuario_modulo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    anio_lectivo = models.ForeignKey(Anio_lectivo, on_delete=models.CASCADE)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    class Meta:
        ordering = ['usuario']
    def __str__(self):
        return '{}'.format(self.usuario)

#ORDERING Y STR revisar
class Respuesta_encuesta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    class Meta:
        ordering = ['fecha']
    def __str__(self):
        return '{}'.format(self.fecha)

#ORDERING Y STR revisar
class Detalle_respuesta(models.Model):
    valor = models.CharField(max_length=100)
    respuesta_encuesta = models.ForeignKey(Respuesta_encuesta, on_delete = models.CASCADE)
    usuario_modulo = models.ForeignKey(Usuario_modulo, on_delete=models.CASCADE)
    pregunta_encuesta = models.ForeignKey(Pregunta_Encuesta, on_delete = models.CASCADE)
    class Meta:
        ordering = ['valor']
    def __str__(self):
        return '{}'.format(self.valor)



