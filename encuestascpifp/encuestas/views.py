from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Pregunta, Usuario, User
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.core.exceptions import PermissionDenied

from django.utils import timezone

from .forms import PreguntaForm, UsuarioForm

@login_required
def index(request):
    if request.method=='POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            preguntaAGuardar = form.save(commit=False)
            preguntaAGuardar.save()
        return redirect('encuestas:index')
    else: 
        #lista_ultimas_preguntas=Pregunta.objects.order_by('-fecha_pub')[:5]
        lista_preguntas = Pregunta.objects.all()
        contexto ={
            'lista_preguntas': lista_preguntas
        }
        return render(request,'encuestas/index.html',contexto)
    
@login_required
def detalle_pregunta(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    return render(request,'encuestas/detallePregunta.html',{'pregunta':pregunta})
@login_required
def tipo_pregunta(request, id_tipo_pregunta_enc):
    return HttpResponse("Id de la pregunta: %s" % id_tipo_pregunta_enc)
@login_required
def pregunta(request, id_pregunta):
    return HttpResponse("Está respondiendo a la pregunta: %s" % id_pregunta)
@login_required
def opcion_pregunta(request, id_opc_pregunta):
    return HttpResponse("Opción: %s" % id_opc_pregunta)

@login_required
def pregunta_delete(request,id_pregunta):

    pregunta = Pregunta.objects.get(id=id_pregunta)
    if not request.user.is_superuser:
        raise PermissionDenied

    if request.method =='POST':
        pregunta.delete()
        return redirect('encuestas:index')
    else:
        contexto = {'pregunta':pregunta}
        return render(request,'encuestas/pregunta_delete.html',contexto)

@login_required
def pregunta_create(request):

    if not request.user.is_superuser:
        raise PermissionDenied

    if request.method =='POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('encuestas:index')
    else:
        form = PreguntaForm()
        pregunta = Pregunta.objects.all()
        contexto = {'form':form,'pregunta':pregunta}
        return render(request,'encuestas/pregunta_create.html',contexto)

@login_required
def pregunta_update(request,id_pregunta):
    if not request.user.is_superuser:
        raise PermissionDenied

    pregunta = Pregunta.objects.get(id=id_pregunta)
    if request.method == "GET":
        pregunta.delete()
        form = PreguntaForm(instance=pregunta)
        preguntas = Pregunta.objects.all()
        contexto = {'form':form,'preguntas':preguntas,'pregunta':pregunta}
        return render(request,'encuestas/pregunta_update.html',contexto)
    else:
        form = PreguntaForm(request.POST,instance=pregunta)
        if form.is_valid():
            form.save()
        return redirect('encuestas:index')


@login_required
def usuarios(request,user): 
    usuario = get_object_or_404(User, pk=user)
    return render(request,'encuestas/usuarios.html',{'usuario':usuario})

@login_required
def usuario_create(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    if request.method =='POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('encuestas:index')
    
   # if request.POST["Cancelar"]:
    #    return redirect('encuestas:index')

    else:
        form = UsuarioForm()
        usuario = Usuario.objects.all()
        contexto = {'form':form,'usuario':usuario}
        return render(request,'encuestas/usuario_create.html',contexto)














'''
@login_required
def votar (request, pregunta_id):
    Pregunta = get_object_or_404 (Pregunta, pk = pregunta_id)
    form = ChoiceCommentForm (request.POST or None)
    try:
        opcion_seleccionada = pregunta.opcion_set.get (pk = request.POST ['opcion'])
    except (KeyError, Choice.DoesNotExist):
        return render (request, '', {
            'pregunta': pregunta,
            'error_message': "Seleccione una opcion",
        })
    else:
        selected_choice.votes + = 1
        selected_choice.save ()
        form.save ()
        context = {
        'comment_ichiran': selected_choice,
        }
        return HttpResponseRedirect (reverse ('polls: results', args = (question.id,)), context)
        
'''
        
