from django.shortcuts import render
from django.http import HttpResponse, request
from gestionVotos.models import Acta
from django.db.models import Count, Sum
from django.core.mail import send_mail
from django.conf import settings
from gestionVotos.forms import FormularioContacto, FormularioActa

# Create your views here.
def home(request):
    return render(request,"home.html")
def busquedas_actas(request):
    return render(request,"busquedasActas.html")
def buscar(resquest):

    if resquest.GET["acta"]:
    
        #mensaje= "Articulo Buscados %r" %resquest.GET["acta"]
        acta= resquest.GET["acta"]
        if len(acta) > 20:
            mensaje="texto de busqueda demasiado largo"
        else:
            actas= Acta.objects.filter(tipo_casilla__icontains=acta)
            total_cheloCano= Acta.objects.aggregate(total= Sum('num_votoChelo'))
            total_morena= Acta.objects.aggregate(total= Sum('num_votoMorena')) 
            total_PRD= Acta.objects.aggregate(total= Sum('num_prd')) 
            total_PRI= Acta.objects.aggregate(total= Sum('num_pri')) 
            total_PT= Acta.objects.aggregate(total= Sum('num_pt'))

          
            #es como si usara el  like
            return render(resquest, "resultados_busquedas.html",{"acta1":total_cheloCano['total'],"query":acta},{"acta1":total_cheloCano['total'],"query":acta} )
    else:
        mensaje= "no ha introducido nada "
    return HttpResponse(mensaje)
def contacto(request):
    if request.method=="POST":
        miFormlario= FormularioContacto(request.POST)
        if miFormlario.is_valid():
            intForm= miFormlario.cleaned_data
            send_mail(intForm['asunto'],intForm['mensaje'],
            intForm.get('email',''),['rmatico13@hotmal.com'])
            
            return render(request,"gracias.html")
    else:
        miFormlario= FormularioContacto()
    return render(request,"formulario_contacto.html",{"form":miFormlario})
    '''
        subject= request.POST["asunto"]
        message= request.POST["mensaje"] +" " + request.POST["email"]
        email_from= settings.EMAIL_HOST_USER
        recipient_list=["pcivilcunduacan@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)
    return render(request,"contacto.html")
    '''
def resultados_votaciones(request):

    
    #total_cheloCano= Acta.objects.aggregate(total= Sum('num_votoChelo'))
    total_cheloCano= Acta.objects.aggregate(total= Sum('num_votoChelo'))
    total_morena= Acta.objects.aggregate(total= Sum('num_votoMorena')) 
    total_PRD= Acta.objects.aggregate(total= Sum('num_prd')) 
    total_PRI= Acta.objects.aggregate(total= Sum('num_pri')) 
    total_PT= Acta.objects.aggregate(total= Sum('num_pt'))
    total_votos= Acta.objects.aggregate(total= Sum('total_votos'))
    
    #total_cheloCano= Acta.objects.filter(610).aggregate(total= Sum('num_votoChelo'))    

        #return render(request,"resultadosActas.html",{"form":miFormulalarioActa,"resultado_cano":total_cheloCano['total'],"resultado_oscar":total_morena['total'],"resultado_homero":total_PRD['total'],"resultado_aurora":total_PRI['total'],"resultado_joaquin":total_PT['total'],"total_votos":total_votos['total']})
    
    if request.method=="POST":
        miFormulalarioActa= FormularioActa(request.POST)
        if miFormulalarioActa.is_valid():
            intForm= miFormulalarioActa.cleaned_data
            seccion_buscar=intForm.get('seccion')
            #con el metodo.get recupero la informacion que se esta dando en el formulario
            #resul_seccion(seccion)
            total_cheloCano= Acta.objects.filter(seccion=seccion_buscar).aggregate(total= Sum('num_votoChelo'))
            total_morena= Acta.objects.filter(seccion=seccion_buscar).aggregate(total= Sum('num_votoMorena'))
            total_PRD= Acta.objects.filter(seccion=seccion_buscar).aggregate(total= Sum('num_prd'))
            total_PRI= Acta.objects.filter(seccion=seccion_buscar).aggregate(total= Sum('num_pri'))
            total_PT= Acta.objects.filter(seccion=seccion_buscar).aggregate(total= Sum('num_pt'))
            total_votos= Acta.objects.filter(seccion=seccion_buscar).aggregate(total= Sum('total_votos'))
    else:
        miFormulalarioActa= FormularioActa()
        

    return render(request,"resultadosActas.html",{"form":miFormulalarioActa,"resultado_cano":total_cheloCano['total'],"resultado_oscar":total_morena['total'],"resultado_homero":total_PRD['total'],"resultado_aurora":total_PRI['total'],"resultado_joaquin":total_PT['total'],"total_votos":total_votos['total']})
    print(Acta.objects.aggregate(total= Sum('total_votos')))
    print (Acta.objects.filter(seccion=610).aggregate(total= Sum('num_votoMorena')))
#def totalvotos(request):
 #   return render()