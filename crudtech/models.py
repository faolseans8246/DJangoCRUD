from django.db import models

# Create your models here.

# Bazani shakllantirish qismi
class MyBase(models.Model):

    login = models.CharField(max_length=100,)
    parol = models.CharField(max_length=128)
    email = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    year = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.login
