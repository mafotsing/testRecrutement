from django.urls import path
from .views import *

urlpatterns = [
    path('update/<int:pk>/', UpdateEmployee.as_view()),
    path('list', ListEmployee.as_view()),
    path('create', CreateEmployee.as_view()),
    path('delete/<int:pk>/', DeleteEmployee.as_view()),
     path('updateClient/<int:pk>/', UpdateClient.as_view()),
    path('listClient', ListClient.as_view()),
    path('createClient', CreateClient.as_view()),
    path('deleteClient/<int:pk>/', DeleteClient.as_view()),
]
