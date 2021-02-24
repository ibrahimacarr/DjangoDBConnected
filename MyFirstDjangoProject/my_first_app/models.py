from django.db import models

# Create your models here.

class User(models.Model):
    Name = models.CharField(max_length = 20)
    Surname = models.CharField(max_length = 20)
    BirthDate = models.DateField()
    Plate = models.CharField(max_length=20)

    def __str__(self):
        return str(self.Name)

class Car(models.Model):
    Plate = models.ForeignKey(User, on_delete = models.CASCADE)
    Model = models.CharField(max_length=50)

    def __str__(self):
        return str(self.Model)
