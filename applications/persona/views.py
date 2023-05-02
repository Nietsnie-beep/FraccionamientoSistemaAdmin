from django.shortcuts import render
from django.views.generic import ListView

from rest_framework import generics

from .models import Person

from .serializers import PersonSerializers

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