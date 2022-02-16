from statistics import mode
from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
from django.utils import timezone
<<<<<<< HEAD
from django.urls import reverse
=======
>>>>>>> f9be4cb (ingredients show correctly on detail page, delete cocktail, and order by date created)
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

    class Meta:
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name 

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('categories_index')


class Drink(models.Model):
    drink_id = models.CharField(max_length=10)
    drink_name = models.CharField(max_length=100)
    drink_instructions = models.TextField(max_length=500)
    drink_pic = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)
    users = models.ManyToManyField(User)
    created_date = models.DateTimeField('date created', default=timezone.now)
<<<<<<< HEAD
    categories = models.ManyToManyField(Category)
=======
>>>>>>> f9be4cb (ingredients show correctly on detail page, delete cocktail, and order by date created)
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
   
class Photo(models.Model):
  url = models.CharField(max_length=200)
  drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

  def get_absolute_url(self):
        return reverse('drink_details')

  def __str__(self):
    return f'Photo for drink_id: {self.drink_id} @{self.url}'