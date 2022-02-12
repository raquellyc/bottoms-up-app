from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import LIQUORS, Drink, Survey
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
    if request.POST['liquor_pref'] == LIQUORS[0][0]:
        cocktail = requests.get('https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=vodka').json()
        print(cocktail)
    elif request.POST['liquor_pref'] == 'G':
        cocktail = requests.get('https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=gin').json()
        print(cocktail)
    elif request.POST['liquor_pref'] == 'R':
        cocktail = requests.get('https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=rum').json()
        print(cocktail)
    elif request.POST['liquor_pref'] == 'T':
        cocktail = requests.get('https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=tequila').json()
        print(cocktail)
    else:
        cocktail =  'None'
    print(cocktail)

 
    return render(request, 'drinks/todays_cocktail.html', {'cocktail': cocktail })

# Class-Based View (CBV)
class SurveyForm(LoginRequiredMixin, CreateView):
  model = Survey
  fields = ['liquor_pref', 'q1', 'q2', 'q3']
