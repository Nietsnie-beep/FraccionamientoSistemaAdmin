from django.shortcuts import render
from django.views.generic import ListView

from rest_framework import generics

from .models import Person, Carros, Provedor, Gastos, Area_comun, reserva

from .serializers import PersonSerializers, CarroSerializers, ProvedorSerializers,GastosSerializers, Area_comunSerializers, reservaSerializers

#####____________casa_______________________#####
class ListPersons(ListView): 
    template_name = 'persona/personas.html'
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()
    
class PersonListApiView(generics.ListAPIView):

    serializer_class = PersonSerializers

    def get_queryset(self):
        return Person.objects.all()
    
class PersonSearchApiView(generics.ListAPIView):
    serializer_class = PersonSerializers

    def get_queryset(self):
        kword = self.kwargs['kword']
        return Person.objects.filter(
            Nombre_Residente__icontains=kword
        )
    
class PersonCreateView(generics.CreateAPIView):
    serializer_class = PersonSerializers

#detail - view
class PersonDetailView(generics.RetrieveAPIView):    
    serializer_class = PersonSerializers
    queryset = Person.objects.filter()


class PersonDeleteView(generics.DestroyAPIView):
    serializer_class = PersonSerializers
    queryset = Person.objects.all()


class PersonUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = PersonSerializers
    queryset = Person.objects.all()


############################______________Carro_____________________###########################################

class CarrosListApiView(generics.ListAPIView):

    serializer_class = CarroSerializers

    def get_queryset(self):
        return Carros.objects.all()
    
class CarroCreateView(generics.CreateAPIView):
    serializer_class = CarroSerializers

class CarroDetailView(generics.RetrieveAPIView):    
    serializer_class = CarroSerializers
    queryset = Carros.objects.filter()

class CarroDeleteView(generics.DestroyAPIView):
    serializer_class = CarroSerializers
    queryset = Carros.objects.all()


class CarroUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = CarroSerializers
    queryset = Carros.objects.all()



#_________________________Provedores________________________________#
class ProvedorListApiView(generics.ListAPIView):

    serializer_class = ProvedorSerializers

    def get_queryset(self):
        return Provedor.objects.all()
    
class ProvedorCreateView(generics.CreateAPIView):
    serializer_class = ProvedorSerializers

class ProvedorDetailView(generics.RetrieveAPIView):    
    serializer_class = ProvedorSerializers
    queryset = Provedor.objects.filter()

class ProvedorDeleteView(generics.DestroyAPIView):
    serializer_class = ProvedorSerializers
    queryset = Provedor.objects.all()


class ProvedorUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ProvedorSerializers
    queryset = Provedor.objects.all()


#_________________________Gastos________________________________#
class GastosListApiView(generics.ListAPIView):

    serializer_class = GastosSerializers

    def get_queryset(self):
        return Gastos.objects.all()
    
class GastosCreateView(generics.CreateAPIView):
    serializer_class = GastosSerializers

class GastosDetailView(generics.RetrieveAPIView):    
    serializer_class = GastosSerializers
    queryset = Gastos.objects.filter()

class GastosDeleteView(generics.DestroyAPIView):
    serializer_class = GastosSerializers
    queryset = Gastos.objects.all()


class GastosUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = GastosSerializers
    queryset = Gastos.objects.all()

#_________________________Area_comun________________________________#
class Area_comunListApiView(generics.ListAPIView):

    serializer_class = Area_comunSerializers

    def get_queryset(self):
        return Area_comun.objects.all()
    
class Area_comunCreateView(generics.CreateAPIView):
    serializer_class = Area_comunSerializers

class Area_comunDetailView(generics.RetrieveAPIView):    
    serializer_class = Area_comunSerializers
    queryset = Area_comun.objects.filter()

class Area_comunDeleteView(generics.DestroyAPIView):
    serializer_class = Area_comunSerializers
    queryset = Area_comun.objects.all()


class Area_comunUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = Area_comunSerializers
    queryset = Area_comun.objects.all()



#_________________________Reserva________________________________#
class reservaListApiView(generics.ListAPIView):

    serializer_class = reservaSerializers

    def get_queryset(self):
        return reserva.objects.all()
    
class reservaCreateView(generics.CreateAPIView):
    serializer_class = reservaSerializers

class reservaDetailView(generics.RetrieveAPIView):    
    serializer_class = reservaSerializers
    queryset = reserva.objects.filter()

class reservaDeleteView(generics.DestroyAPIView):
    serializer_class = reservaSerializers
    queryset = reserva.objects.all()


class reservaUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = reservaSerializers
    queryset = reserva.objects.all()
