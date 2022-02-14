from email.policy import default
import json
from operator import index
from pyexpat import model
from typing import final
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ANSWERS1, LIQUORS, Drink, Survey
import requests, random 
# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def drinks_index(request):
  drinks = Drink.objects.all()
  return render(request, 'drinks/index.html', {'drinks': drinks})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def generate_drink(request):
    if request.POST['liquor_pref'] == LIQUORS[0][0]:
        cocktails_by_ingredient = requests.get('https://www.thecocktaildb.com/api/json/v2/9973533/filter.php?i=vodka').json()
      
    elif request.POST['liquor_pref'] == 'G':
        cocktails_by_ingredient = requests.get('https://www.thecocktaildb.com/api/json/v2/9973533/filter.php?i=gin').json() 
    elif request.POST['liquor_pref'] == 'R':
        cocktails_by_ingredient = requests.get('https://www.thecocktaildb.com/api/json/v2/9973533/filter.php?i=rum').json()  
    elif request.POST['liquor_pref'] == 'T':
        cocktails_by_ingredient = requests.get('https://www.thecocktaildb.com/api/json/v2/9973533/filter.php?i=tequila').json()
    else:
       cocktails_by_ingredient =  'None'

    all_drinks = cocktails_by_ingredient['drinks']
    index_list = []
    for all_ids in all_drinks:
        ingredient_choice_ids = all_ids['idDrink']
        index_list.append(ingredient_choice_ids) 

    if request.POST['q1'] == ANSWERS1[0][0]:
        cocktails_by_category = requests.get('https://www.thecocktaildb.com/api/json/v2/9973533/filter.php?c=ordinary_drink').json()
    elif request.POST['q1'] == 'P':
        cocktails_by_category = requests.get('https://www.thecocktaildb.com/api/json/v2/9973533/filter.php?c=cocktail').json()

    all_category_drinks = cocktails_by_category['drinks']
    index_list2 = []
    for all_ids in all_category_drinks:
        category_choice_ids = all_ids['idDrink']
        index_list2.append(category_choice_ids) 
    # print(index_list2)

    index_list3 = []
    for id in index_list:
      if id in index_list2:
        index_list3.append(id)
    # print(index_list3)

    drink_id = random.choice(index_list3)
    print(drink_id)
    final_drink_render = requests.get('https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=' + drink_id ).json()
    # print(final_drink_render)

    drink_name = final_drink_render['drinks'][0]['strDrink']
    drink_instructions = final_drink_render['drinks'][0]['strInstructions']
    drink_pic = final_drink_render['drinks'][0]['strDrinkThumb']
    drink_ingredient1 = final_drink_render['drinks'][0]['strIngredient1']
    drink_ingredient2 = final_drink_render['drinks'][0]['strIngredient2']
    drink_ingredient3 = final_drink_render['drinks'][0]['strIngredient3']
    drink_ingredient4 = final_drink_render['drinks'][0]['strIngredient4']
    drink_ingredient5 = final_drink_render['drinks'][0]['strIngredient5']
    drink_ingredient6 = final_drink_render['drinks'][0]['strIngredient6']
    drink_ingredient7 = final_drink_render['drinks'][0]['strIngredient7']
    drink_ingredient8 = final_drink_render['drinks'][0]['strIngredient8']
    
    return render(request, 'drinks/todays_cocktail.html', {
        'cocktails_by_ingredient': cocktails_by_ingredient,
        'drink_id': drink_id, 
        'drink_name': drink_name, 
        'drink_instructions': drink_instructions, 
        'drink_pic': drink_pic,
        'drink_ingredient1': drink_ingredient1,
        'drink_ingredient2': drink_ingredient2,
        'drink_ingredient3': drink_ingredient3,
        'drink_ingredient4': drink_ingredient4,
        'drink_ingredient5': drink_ingredient5,
        'drink_ingredient6': drink_ingredient6,
        'drink_ingredient7': drink_ingredient7,
        'drink_ingredient8': drink_ingredient8,
    })

def add_drink(request):
  # form = SurveyForm(request.POST)
  # form.save()
  drinkDataFromAPI = [
    {'drink_id': request.POST['id']},
    {'drink_name': request.POST['name']},
    {'drink_instructions': request.POST['instructions']},
    {'drink_pic': request.POST['pic']},
    {'drink_ingredient1': request.POST['drink_ingredient1']},
    {'drink_ingredient2': request.POST['drink_ingredient2']},
    {'drink_ingredient3': request.POST['drink_ingredient3']},
    {'drink_ingredient4': request.POST['drink_ingredient4']},
    {'drink_ingredient5': request.POST['drink_ingredient5']},
    {'drink_ingredient6': request.POST['drink_ingredient6']},
    {'drink_ingredient7': request.POST['drink_ingredient7']},
    {'drink_ingredient8': request.POST['drink_ingredient8']},
  ]
  drink_ingredients = []
  if drinkDataFromAPI[4].get('drink_ingredient1') != 'None':
    drink_ingredients.append(drinkDataFromAPI[4])
  if drinkDataFromAPI[5].get('drink_ingredient2') != 'None':
    drink_ingredients.append(drinkDataFromAPI[5])
  if drinkDataFromAPI[6].get('drink_ingredient3') != 'None':
    drink_ingredients.append(drinkDataFromAPI[6])
  if drinkDataFromAPI[7].get('drink_ingredient4') != 'None':
    drink_ingredients.append(drinkDataFromAPI[7])
  if drinkDataFromAPI[8].get('drink_ingredient5') != 'None':
    drink_ingredients.append(drinkDataFromAPI[8])
  if drinkDataFromAPI[9].get('drink_ingredient6') != 'None':
    drink_ingredients.append(drinkDataFromAPI[9])
  if drinkDataFromAPI[10].get('drink_ingredient7') != 'None':
    drink_ingredients.append(drinkDataFromAPI[10])
  if drinkDataFromAPI[11].get('drink_ingredient8') != 'None':
    drink_ingredients.append(drinkDataFromAPI[11])

  formatted_data_from_API = []
  formatted_data_from_API.append(drinkDataFromAPI[0])
  formatted_data_from_API.append(drinkDataFromAPI[1])
  formatted_data_from_API.append(drinkDataFromAPI[2])
  formatted_data_from_API.append(drinkDataFromAPI[3])
  formatted_data_from_API.append(drink_ingredients)
  print(formatted_data_from_API)
  
  return redirect('index')




# Class-Based View (CBV)
class SurveyForm(LoginRequiredMixin, CreateView):
  model = Survey
  fields = ['liquor_pref', 'q1', 'q2', 'q3']

# class CreateDrink(CreateView):
#   model = Drink 
#   fields = '__all__'
#   success_url = '/drinks/'
