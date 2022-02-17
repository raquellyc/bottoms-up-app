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
    path('drinks/<int:drink_id>/', views.drink_detail, name='drink_detail'),
    path('drinks/<int:pk>/delete/', views.DrinkDelete.as_view(), name='drink_delete'),
    path('drinks/<int:drink_id>/assoc_category/<int:category_id>/', views.assoc_category, name="add_category"),
    path('drinks/<int:drink_id>/unassoc_category/<int:category_id>/', views.unassoc_category, name="remove_category"),
    path('drinks/<int:drink_id>/add_photo/', views.add_photo, name='add_photo'),      
    path('photo/<int:pk>/delete/', views.PhotoDelete.as_view(), name='photo_delete'),
    path('categories/', views.CategoryList.as_view(), name="categories_index"),
    path('categories/create/', views.CategoryCreate.as_view(), name="categories_create"),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name="categories_detail"),
    path('categories/<int:pk>/update/', views.CategoryUpdate.as_view(), name="categories_update"),
    path('categories/<int:pk>/delete/', views.CategoryDelete.as_view(), name="categories_delete"),
]