from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('about/', views.about, name="about"),
    path('book/', views.bookPage, name='book'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('signup/', views.signup, name='signup'),
    path('book/<int:book_id>/download/', views.download_book, name='download_book'),
    path('logout/', views.logout, name="logout")

]
