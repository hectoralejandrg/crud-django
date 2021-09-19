from django.db import models

class Escuela(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=200)
    district = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'
