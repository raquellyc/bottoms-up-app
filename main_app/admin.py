from django.contrib import admin
from .models import Drink, Ingredient, Survey
# Register your models here.
admin.site.register(Drink)
admin.site.register(Survey)
admin.site.register(Ingredient)