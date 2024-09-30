from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.CharField(max_length=4)
    n_employees = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True, null=False)
    price = models.IntegerField()
    serial_number = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    year_prod = models.CharField(max_length=4)
    kilometres = models.IntegerField()
    TYPES = {
        "S" : "SEDAN",
        "SU" : "SUV",
        "H" : "HATCHBACK",
        "C" : "COUPE",
    }
    image = models.ImageField(upload_to="images/", blank=True, null=True)
