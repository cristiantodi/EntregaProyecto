from django.db import models

# Create your models here.

class event(models.Model):
    event           =   models.TextField(blank=True, null=True)

    class Meta:
        verbose_name='Evento'
        verbose_name_plural='Eventos'

    def __str__(self):
        return self.event 
    


class Model_sistem(models.Model):
    model           =   models.CharField(max_length=200, blank=True, null=True)
    os              =   models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name='Tipo_equipo'
        verbose_name_plural='Tipos_equipos'

    def __str__(self):
        return self.model

class equipment(models.Model):
    date            =   models.DateField(blank=True, null=True)
    time            =   models.TimeField(blank=True, null=True)
    type_equipment  =   models.ForeignKey(Model_sistem, blank=True, null=True, on_delete=models.CASCADE) 
    location        =   models.CharField(max_length=200, blank=True, null=True)
    user            =   models.CharField(max_length=200, blank=True, null=True)
    event           =   models.ForeignKey(event, blank=True, null=True, on_delete=models.CASCADE) 

    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name='Equipo'
        verbose_name_plural='Equipos'
