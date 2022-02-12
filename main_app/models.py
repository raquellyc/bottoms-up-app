from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Drink(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField(max_length=250)
    instructions = models.TextField(max_length=250)
    image = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.id})'



# class Survey(models.Model):
#     liquor_pref = models.CharField(max_length=7)
#     q1 = models.CharField(max_length=3)
#     q2 = models.CharField(max_length=4)
#     q3 = models.CharField(max_length=12)
#     q4 = models.CharField(max_length=12)
    
