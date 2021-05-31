from django.db import models

# Create your models here.
class Acta(models.Model):
    seccion= models.CharField(max_length=6)
    tipo_casilla= models.CharField(max_length=30)
    num_votoChelo=models.IntegerField(verbose_name="INDEPENDIENTE, JESUS ABRAHAM CANO GONZALEZ")
    num_votoMorena=models.IntegerField(verbose_name="MORENA, OSCAR ENRIQUE RAMOS MENDEZ")
    num_prd=models.IntegerField(verbose_name="PRD, HOMERO YAÑEZ RUIZ")
    num_pri=models.IntegerField(verbose_name="PRI/PAN(COALICIO), AURORA PIÑERA FERNANDEZ")
    num_pt=models.IntegerField(verbose_name="PT, JOAQUIN ANTONIO SOLIS MENDOZA")
    num_verde=models.IntegerField(verbose_name="PARTIDO VERDE ECOLOGISTA,JUANA DEL CARMEN LOPEZ GRANIER")
    num_movimientociudadano=models.IntegerField(verbose_name="MOVIMIENTO CIUDADANO, PATRICIA ELEJO ALMEIDA")
    num_encuentrosolidario=models.IntegerField(verbose_name="PARTIDO ENCUENTRO SOLIDARIO")
    num_redesSociales=models.IntegerField(verbose_name="REDES SOCIALES PROGRECISTAS, FRANCISCO PEREZ PONSE")
    num_fuerzaMexico= models.IntegerField(verbose_name="FUERZA POR MEXICO, MARIA LUZ GALLEGO VAZQUEZ")
    num_candidatosNoRegistrados=models.IntegerField(verbose_name="CANDIDATOS NO REGISTRADOS")
    num_votoNulos=models.IntegerField(verbose_name="VOTOS NULOS")
    total_votos= models.IntegerField(verbose_name="TOTAL DE VOTOS")
    def __str__(self):
        return 'el numero total que tiene es %s y el numero que da  la sumatoria es %s'%(self.total_votos, self.sumaVotos())

    def sumaVotos(self):  
        return  self.num_votoChelo + self.num_votoMorena+self.num_prd+self.num_pri+self.num_pt+self.num_verde+self.num_movimientociudadano+self.num_encuentrosolidario+self.num_redesSociales+self.num_fuerzaMexico+self.num_candidatosNoRegistrados+self.num_votoNulos
    
class Politico(models.Model):
    nombre= models.CharField(max_length=30)
    edad= models.CharField(max_length=30)
    direccion= models.CharField(max_length=30)
    partidoPolitico= models.CharField(max_length=30)
    correo= models.EmailField(blank=True)
    fecha= models.DateField(null=True)
    def __str__(self): 

        return 'el nombre del politico es %s la edad es %s su direccion es %s  del partido politico %s con correo %s'%(self.nombre,self.edad,self.direccion,self.partidoPolitico,self.correo)