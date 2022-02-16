from django.contrib import admin
from .models import Category, Drink, Ingredient, Survey
# Register your models here.
admin.site.register(Drink)
admin.site.register(Survey)
admin.site.register(Ingredient)
admin.site.register(Category)