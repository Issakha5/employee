from django.db import models

# Create your models here.


class Employee(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    email = models.EmailField()
    adress = models.CharField(max_length=200)

    def __str__(self):
        return self.nom
