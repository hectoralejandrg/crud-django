from django.db import models

from clase.models import Clase
from escuela.models import Escuela


class Student(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    address = models.TextField(max_length=200)
    dob = models.DateField()
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    escuela = models.ForeignKey(
        Escuela,
        related_name='student',
        on_delete=models.SET_NULL,
        null=True
    )
    clase = models.ManyToManyField(
        Clase,
        related_name='clase'
    )

    def __str__(self):
        return f'{self.name} {self.lastname} - {self.email}'
