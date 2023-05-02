from rest_framework import serializers
from .models import Person, Carros,Provedor, Gastos, Area_comun, reserva,Pagos_pendientes

class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person  
        fields = '__all__'


class CarroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Carros  
        fields = '__all__'


class ProvedorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Provedor
        fields = '__all__'

class GastosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Gastos
        fields = '__all__'

class Area_comunSerializers(serializers.ModelSerializer):
    class Meta:
        model = Area_comun
        fields = '__all__'

class reservaSerializers(serializers.ModelSerializer):
    class Meta:
        model = reserva
        fields = '__all__'

class Pagos_pendientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pagos_pendientes
        fields = '__all__'