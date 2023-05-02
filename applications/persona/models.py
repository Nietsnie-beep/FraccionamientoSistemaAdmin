#
from model_utils.models import TimeStampedModel
#
from django.db import models


#

Home_status = [
    (1, 'En Renta'),
    (2, 'En venta')
]

Tipo_pago = [
    (1, 'efectivo'),
    (2, 'Tarjeta')
]
class Person(TimeStampedModel):
    """  Modelo para registrar casas de una agenda  """

    Calle = models.CharField(
        max_length=120,
    )
    Numero = models.IntegerField()
  
    Mts = models.CharField(
            max_length=50,
        )
    
    Propietario = models.CharField(
            max_length=50,
        )
    
    Telefono_Propietario = models.CharField(
            max_length=50,
        )
    
    Nombre_Residente = models.CharField(
            max_length=50,
        )
    
    Telefono_contacto = models.CharField(
            max_length=50,  
    )
    Status = models.IntegerField(
        blank=True,
        choices=Home_status,
        default=1
    )

    email = models.EmailField(
        blank=True, 
        null=True
    )
    phone = models.CharField(
        max_length=15,
        blank=True,
    )

    house_notes = models.CharField(
        max_length=150,
        blank=True,

    )

    bloqueo = models.BooleanField(
        default=False
    )

    area = models.CharField(
        max_length=150,
        blank=True
    )

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
    
    def __str__(self):
        return self.Calle + ' ' + str(self.Numero)



class Carros(TimeStampedModel):

    marca = models.CharField(
        max_length=50
    )

    color = models.CharField(
        max_length=50
    )

    tag = models.CharField(
        max_length=50
    )

    modelo = models.CharField(
        max_length=50
    )

    placas = models.CharField(
        max_length=50
    )

    imagen = models.ImageField(upload_to='images/')

    casa = models.ForeignKey(Person, verbose_name="Casa", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
    
    def __str__(self):
        return self.placas
    

class Provedor(models.Model):
    nombre = models.CharField(max_length=50)

    servicio = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Provedor'
        verbose_name_plural = 'Provedores'
    
    def __str__(self):
        return self.nombre
    
class Gastos(TimeStampedModel):
    provedor = models.ForeignKey(Provedor, verbose_name='Provedor', on_delete=models.PROTECT)
    referencia = models.CharField(max_length=150, blank=True)
    Monto = models.CharField(max_length=500,blank=True )
    fecha_limite = models.DateField()
    concepto = models.CharField(max_length=150)
    cuenta_de_pago = models.CharField(max_length=150)
    forma_de_pago = models.IntegerField (
        choices=Tipo_pago,
        default=1
        )


    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'
    
    def __str__(self):
        return str(self.provedor) + ' ' + self.concepto
    
Concepto_pagos = [
    (1, 'Cuotas'),
    (2, 'Penalizacion'),
    (3, 'Multas'),
    (4, 'otros'),
    (5, 'pendiente'),

]

estatus_pago = [
    (1, 'Recargo'),
    (2, 'Pagado'),
    (4, 'otros')
]

#?????
class Pagos_pendientes(TimeStampedModel):
    nombre = models.CharField(max_length=50)
    casa = models.ForeignKey(Person, verbose_name="Casa", on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    fecha_vencimiento = models.DateField()
    concepto = models.IntegerField (
        choices=Concepto_pagos,
        default=5
        )
    recargo = models.IntegerField()
    estatus = models.IntegerField(
        choices=estatus_pago,
        default=1
    )

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
    
    def __str__(self):
        return str(self.casa.Numero) + ' ' + self.nombre
    
class Area_comun(models.Model):
    nombre = models.CharField(max_length=120);
    apertura = models.TimeField()
    cierre = models.TimeField()
    icono = models.ImageField(
        upload_to='images/'
    )


    class Meta:
        verbose_name = 'Areas comunes'
        verbose_name_plural = 'Area comun'
    
    def __str__(self):
        return self.nombre
    
class reserva(TimeStampedModel):
    area = models.ForeignKey(Area_comun, verbose_name="Area", on_delete=models.CASCADE)
    Dia = models.DateField()
    motivo = models.CharField(max_length=100)

    casa = models.ForeignKey(Person, on_delete=models.CASCADE, limit_choices_to={'bloqueo':False})


    class Meta:
        unique_together = ('area', 'casa')
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
    
    def __str__(self):
        return str(self.casa) + ' ' +  str(self.area)