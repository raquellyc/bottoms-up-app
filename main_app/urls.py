from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('drinks/', views.drinks_index, name='index'),
    path('survey/', views.SurveyForm.as_view(), name='survey_form'),
    path('drinks/generate', views.generate_drink, name='generate_drink'),
    path('drinks/add_drink/', views.add_drink, name='add_drink'),
]