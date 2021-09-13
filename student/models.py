from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    address = models.TextField(max_length=200)
    dob = models.DateField()
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} {self.lastname} - {self.email}'


class Class(models.Model):
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'
