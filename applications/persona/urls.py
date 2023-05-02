from django.urls import path, re_path
from . import views

app_name = 'persona_app'


urlpatterns = [
    path(
    'personas/',
    views.ListPersons.as_view(),
    name='personas'
    ),

    path(
    'api/persona/list',
    views.PersonListApiView.as_view()
    ),

    path(
    'api/persona/search/<kword>/',
    views.PersonSearchApiView.as_view()
    ),

    path(
    'api/persona/create',
    views.PersonCreateView.as_view()
    ),

    path(
    'api/persona/detail/<pk>/',
    views.PersonDetailView.as_view()
    ),

     path(
    'api/persona/delete/<pk>/',
    views.PersonDeleteView.as_view()
    ),

      path(
    'api/persona/update/<pk>/',
    views.PersonUpdateView.as_view()
    ),

    ##________________carros________________##
    path(
    'api/carros/list',
    views.CarrosListApiView.as_view()
    ),

     path(
    'api/carros/create',
    views.CarroCreateView.as_view()
    ),

      path(
    'api/carros/detail/<pk>/',
    views.CarroDetailView.as_view()
    ),

       path(
    'api/carros/delete/<pk>/',
    views.CarroDeleteView.as_view()
    ),

        path(
    'api/carros/update/<pk>/',
    views.CarroUpdateView.as_view()
    ),
    
     ##________________Provedor________________##

      path(
    'api/provedor/list',
    views.ProvedorListApiView.as_view()
    ),

     path(
    'api/provedor/create',
    views.ProvedorCreateView.as_view()
    ),

      path(
    'api/provedor/detail/<pk>/',
    views.ProvedorDetailView.as_view()
    ),

       path(
    'api/provedor/delete/<pk>/',
    views.ProvedorDeleteView.as_view()
    ),

        path(
    'api/provedor/update/<pk>/',
    views.ProvedorUpdateView.as_view()
    ),


         ##________________Gastos________________##

      path(
    'api/Gastos/list',
    views.GastosListApiView.as_view()
    ),

     path(
    'api/Gastos/create',
    views.GastosCreateView.as_view()
    ),

      path(
    'api/Gastos/detail/<pk>/',
    views.GastosDetailView.as_view()
    ),

       path(
    'api/Gastos/delete/<pk>/',
    views.GastosDeleteView.as_view()
    ),

        path(
    'api/Gastos/update/<pk>/',
    views.GastosUpdateView.as_view()
    ),


    ##________________Area_comun________________##

      path(
    'api/Area_comun/list',
    views.Area_comunListApiView.as_view()
    ),

     path(
    'api/Area_comun/create',
    views.Area_comunCreateView.as_view()
    ),

      path(
    'api/Area_comun/detail/<pk>/',
    views.Area_comunDetailView.as_view()
    ),

       path(
    'api/Area_comun/delete/<pk>/',
    views.Area_comunDeleteView.as_view()
    ),

        path(
    'api/Area_comun/update/<pk>/',
    views.Area_comunUpdateView.as_view()
    ),

        ##________________Reserva________________##

      path(
    'api/reserva/list',
    views.reservaListApiView.as_view()
    ),

     path(
    'api/reserva/create',
    views.reservaCreateView.as_view()
    ),

      path(
    'api/reserva/detail/<pk>/',
    views.reservaDetailView.as_view()
    ),

       path(
    'api/reserva/delete/<pk>/',
    views.reservaDeleteView.as_view()
    ),

        path(
    'api/reserva/update/<pk>/',
    views.reservaUpdateView.as_view()
    ),


        ##________________Pagos_pendientes________________##

      path(
    'api/Pagos_pendientes/list',
    views.Pagos_pendientesListApiView.as_view()
    ),

     path(
    'api/Pagos_pendientes/create',
    views.Pagos_pendientesCreateView.as_view()
    ),

      path(
    'api/Pagos_pendientes/detail/<pk>/',
    views.Pagos_pendientesDetailView.as_view()
    ),

       path(
    'api/Pagos_pendientes/delete/<pk>/',
    views.Pagos_pendientesDeleteView.as_view()
    ),

        path(
    'api/Pagos_pendientes/update/<pk>/',
    views.Pagos_pendientesUpdateView.as_view()
    ),
]


