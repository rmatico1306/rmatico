from django.contrib import admin

# Register your models here.
from gestionVotos.models import Acta, Politico
#configuracion para desplegar  la busquedas 
class ActaAdmin(admin.ModelAdmin):
    list_display=("seccion", "tipo_casilla","num_votoChelo","num_votoMorena","num_prd","num_pri","num_pt",
    "num_verde", "num_movimientociudadano", "num_encuentrosolidario", "num_redesSociales","num_fuerzaMexico",
    "num_candidatosNoRegistrados","num_votoNulos","total_votos")
    search_fields=("seccion",)
    list_filter=("tipo_casilla",)
    
class PoliticoAdmin(admin.ModelAdmin):
    #lo que va mostrar en la tabla
    list_display=("nombre", "edad", "direccion")
    #el filtro de fecha
    list_filter=("fecha",)
    #para la barrra de fechas 
    date_hierarchy="fecha"




admin.site.register(Acta, ActaAdmin)
admin.site.register(Politico,PoliticoAdmin)