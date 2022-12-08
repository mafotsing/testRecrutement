from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from .serializers import *
from .models import * 
from .permissions import IsMyPermission

# crud employee.
class ListEmployee(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes=[IsMyPermission]
    permission_classes = [permissions.DjangoModelPermissions]

class UpdateEmployee(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class CreateEmployee(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DeleteEmployee(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
# crud client.
class ListClient(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
   

class UpdateClient(generics.RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class CreateClient(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class DeleteClient(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

