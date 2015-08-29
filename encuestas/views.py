from django.shortcuts import render, render_to_response, get_object_or_404
from .forms import PersonaModelForm, CapitalSocialModelForm, CapitalFisicoModelForm,GrupoFamiliarModelForm,CapitalHumanoModelForm
from .models import CapitalSocial,CapitalHumano,Persona
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.debug import sensitive_post_parameters
from django.template.response import TemplateResponse
from django.shortcuts import resolve_url


def vistapersona(request):

    form=PersonaModelForm()
    nombre = 'Formulario de persona'
    if request.POST:
        form=PersonaModelForm(request.POST)

        if form.is_valid():
            form.save() 

            return render (request,'exito.html', {'form': form})

    return render(request,'formulario.html', {'form': form,'nombre': nombre})
            
def encuesta(request):

    return render_to_response('entrevista.html', locals(),context_instance=RequestContext(request))

def Social(request, id_capitalsocial=None):
    if id_capitalsocial:
        instance = get_object_or_404(CapitalSocial, id=id_capitalsocial)
    else:
        instance = None
    form = CapitalSocialModelForm(instance=instance)
    nombre = 'Formulario para capital social'
    if request.method == 'POST':
        form = CapitalSocialModelForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return render(request,'exito.html',{'form':form})

            
    return render(request,'formulario.html',{'form':form, 'nombre': nombre})
    





def inicio(request):
    return render(request, 'site_base.html', {})


def capital_fisico(request):
	form=CapitalFisicoModelForm()

	if request.method=="POST":
		form=CapitalFisicoModelForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'exito.html', {})
	return render(request,'formulario.html',{'form': form})

def Grupo_Familiar(request):
    form=GrupoFamiliarModelForm()
    nombre = 'Formulario para Grupo Familiar'
    if request.method=="POST":
        form=GrupoFamiliarModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'exito.html', {})

    return render(request,'formulario.html',{'form': form, 'nombre': nombre})

def mujeres_con_pap(request):
    nombre = 'Porcentaje de mujeres con PAP'
    mujeres_con_pap = Persona.objects.filter(grupo_familiar__entrevista__relevamiento__id=1, sexo='f', capitales_humanos__pap=True)
    mujeres_con_pap=len(mujeres_con_pap)
    mujeres_total=Persona.objects.filter(grupo_familiar__entrevista__relevamiento__id=1, sexo='f')
    mujeres_total=len(mujeres_total)
    total=(mujeres_con_pap/mujeres_total)*100                                    
##    if request.method=="POST":
##        form=CapitalHumanoModelForm(request.POST)
##        if form.is_valid():
##            form.save()
##            return render(request,'exito.html', {})
    return render(request,'pap.html',{'nombre': nombre, 'total': total})
    


