from django.contrib import admin

from .models import Person, Carros, Gastos, Pagos_pendientes, Area_comun, reserva, Provedor

admin.site.register(Person)
admin.site.register(Carros)
admin.site.register(Gastos)
admin.site.register(Pagos_pendientes)
admin.site.register(Area_comun)
admin.site.register(reserva)
admin.site.register(Provedor)



