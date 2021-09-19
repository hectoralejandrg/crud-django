from django.db import models

from escuela.models import Escuela


class Clase(models.Model):
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    active = models.BooleanField(default=True)
    escuela= models.ForeignKey(
        Escuela,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return f'{self.name}'
