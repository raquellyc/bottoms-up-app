from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
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




class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.ingredient_name}'

class Drink(models.Model):
    drink_id = models.CharField(max_length=10)
    drink_name = models.CharField(max_length=100)
    drink_instructions = models.TextField(max_length=500)
    drink_pic = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)
    users = models.ManyToManyField(User)
    def __str__(self):
        return f'{self.drink_name} ({self.drink_id})'


class Survey(models.Model):
    liquor_pref = models.CharField('What is your preferred liquor?',
        max_length=1,
        choices=LIQUORS,
        default=LIQUORS[0][0],
    )
    q1 = models.CharField('Was Today work or play?',
        max_length=1,
        choices=ANSWERS1,
        default=ANSWERS1[0][0],
    )
    q2 = models.CharField('Are you feeling adventurous or classic?',
        max_length=1,
        choices=ANSWERS2,
        default=ANSWERS2[0][0],
    )
    q3 = models.CharField('Do you need a pick-me-up or to relax?',
        max_length=1,
        choices=ANSWERS3,
        default=ANSWERS3[0][0],
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
   
