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
        cocktails_by_ingredient = requests.get('https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=vodka').json()
      
    elif request.POST['liquor_pref'] == 'G':
        cocktails_by_ingredient = requests.get('https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=gin').json() 
    elif request.POST['liquor_pref'] == 'R':
        cocktails_by_ingredient = requests.get('https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=rum').json()  
    elif request.POST['liquor_pref'] == 'T':
        cocktails_by_ingredient = requests.get('https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=tequila').json()
    else:
       cocktails_by_ingredient =  'None'

    all_drinks = cocktails_by_ingredient['drinks']
    index_list = []
    for all_ids in all_drinks:
        ingredient_choice_ids = all_ids['idDrink']
        index_list.append(ingredient_choice_ids) 
    # print(index_list)

    if request.POST['q1'] == ANSWERS1[0][0]:
        cocktails_by_category = requests.get('https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=ordinary_drink').json()
    elif request.POST['q1'] == 'P':
        cocktails_by_category = requests.get('https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=cocktail').json()

    all_category_drinks = cocktails_by_category['drinks']
    index_list2 = []
    for all_ids in all_category_drinks:
        category_choice_ids = all_ids['idDrink']
        index_list2.append(category_choice_ids) 
    print(index_list2)
    # r = random.choice(cocktail['drinks'])
    # drink_id = r['idDrink']
    # print(all_drinks)
    # print(r)
    return render(request, 'drinks/todays_cocktail.html', {
        'cocktails_by_ingredient': cocktails_by_ingredient,
        # 'drink_id': drink_id, 
    })

# Class-Based View (CBV)
class SurveyForm(LoginRequiredMixin, CreateView):
  model = Survey
  fields = ['liquor_pref', 'q1', 'q2', 'q3']
