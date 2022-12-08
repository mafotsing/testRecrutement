from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    contact=models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
class Client(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    contact=models.CharField(max_length=15)

    def __str__(self):
        return self.nom
    

   
