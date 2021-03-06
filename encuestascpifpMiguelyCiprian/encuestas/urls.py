from django.urls import path

from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'encuestas'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_pregunta>/',views.pregunta, name="pregunta"),
    path('updatePregunta/<int:id_pregunta>', views.pregunta_update,name='updatePregunta'),
    
    path('deletePregunta/<int:id_pregunta>',views.pregunta_delete,name='deletePregunta'),
    path('createPregunta/',views.pregunta_create,name='createPregunta'),


    path('accounts/login/', auth_views.LoginView.as_view(template_name='encuestas/login.html'),name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),


    
    path('usuario/<int:user>',views.usuarios,name="usuarios"),

    path('encuestas/',views.encuestas,name="encuestas"),
    path('createEncuesta/',views.encuesta_create,name='encuestaCreate'),
    path('agradecimiento/',views.enviado,name="enviado")

    #path('updateUsuarioAjax/',views.usuario_form_ajax,name='UsuarioFormAjax'),
    #path('pregunta/',views.pregunta_create,name='pregunta'),
    
]