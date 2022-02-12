from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Drink, Survey
import requests

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
    form = SurveyForm()
    cocktail = requests.get('https://www.thecocktaildb.com/api/json/v1/1/random.php').json()
        
    drink_name = cocktail['drinks'][0]['strDrink']
    drink_instructions = cocktail['drinks'][0]['strInstructions']
    drink_pic = cocktail['drinks'][0]['strDrinkThumb']
    drink_ingredient1 = cocktail['drinks'][0]['strIngredient1']
    drink_ingredient2 = cocktail['drinks'][0]['strIngredient2']
    drink_ingredient3 = cocktail['drinks'][0]['strIngredient3']
    drink_ingredient4 = cocktail['drinks'][0]['strIngredient4']
    drink_ingredient5 = cocktail['drinks'][0]['strIngredient5']
    drink_ingredient6 = cocktail['drinks'][0]['strIngredient6']
    drink_ingredient7 = cocktail['drinks'][0]['strIngredient7']
    drink_ingredient8 = cocktail['drinks'][0]['strIngredient8']
    return render(request, 'drinks/todays_cocktail.html', {
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
    # return render(request, 'drinks/todays_cocktail.html', {'form': form})

# Class-Based View (CBV)
class SurveyForm(LoginRequiredMixin, CreateView):
  model = Survey
  fields = ['liquor_pref', 'q1', 'q2', 'q3']
