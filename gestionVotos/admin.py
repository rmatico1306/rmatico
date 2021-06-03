from django.contrib import admin

# Register your models here.
from gestionVotos.models import Acta, Politico
#configuracion para desplegar  la busquedas 
class ActaAdmin(admin.ModelAdmin):
    
    list_display=("seccion", "tipo_casilla","num_votoChelo","num_votoMorena","num_pri",
    "num_prd","num_verde","num_pt","num_movimientociudadano",
    "num_encuentrosolidario","num_redesSociales","num_fuerzaMexico", 
    "num_candidatosNoRegistrados","num_votoNulos","total_votos",
    )
    search_fields=("seccion",)
    list_filter=("tipo_casilla",)
    
    def get_readonly_fields(self, request, obj=None):
        "" "Redefinir esta función para limitar los campos que los usuarios normales pueden modificar" ""
        if request.user.is_superuser:
            self.readonly_fields = []
        else:
            self.readonly_fields = ('seccion','tipo_casilla',)

        return self.readonly_fields
    #readonly_fields = ('seccion',)
    #readonly_fields = ('seccion', 'tipo_casila')
    
class PoliticoAdmin(admin.ModelAdmin):
    #lo que va mostrar en la tabla
    list_display=("nombre", "edad", "direccion")
    #el filtro de fecha
    list_filter=("fecha",)
    #para la barrra de fechas 
    date_hierarchy="fecha"




admin.site.register(Acta, ActaAdmin)
admin.site.register(Politico,PoliticoAdmin)