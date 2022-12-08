from rest_framework import serializers
from .models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','name','email','contact')
        
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('nom','prenom','contact')