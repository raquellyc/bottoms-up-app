from django.db import models
from django.contrib.auth.models import User
# Create your models here.

LIQUORS = (
    ('V', 'Vodka'),
    ('G', 'Gin'),
    ('R', 'Rum'),
    ('T', 'Tequila'),
)

ANSWERS1 = (
    ('W', 'Work'),
    ('P', 'Play'),
)
ANSWERS2 = (
    ('A', 'Adventurous'),
    ('C', 'Classic'),
)
ANSWERS3 = (
    ('P', 'Pick-Me-Up'),
    ('R', 'Relaxation'),
)


class Drink(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField(max_length=250)
    instructions = models.TextField(max_length=250)
    image = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.id})'



class Survey(models.Model):
    liquor_pref = models.CharField(
        max_length=1,
        choices=LIQUORS,
        default=LIQUORS[0][0],
    )
    q1 = models.CharField(
        max_length=1,
        choices=ANSWERS1,
        default=ANSWERS1[0][0],
    )
    q2 = models.CharField(
        max_length=1,
        choices=ANSWERS2,
        default=ANSWERS2[0][0],
    )
    q3 = models.CharField(
        max_length=1,
        choices=ANSWERS3,
        default=ANSWERS3[0][0],
    )
   