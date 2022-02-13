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
    print(index_list3)

    drink_id = random.choice(index_list3)
    print(drink_id)
    final_drink_render = requests.get('https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=' + drink_id ).json()
    print(final_drink_render)

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


# Class-Based View (CBV)
class SurveyForm(LoginRequiredMixin, CreateView):
  model = Survey
  fields = ['liquor_pref', 'q1', 'q2', 'q3']
