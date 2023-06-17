from django.urls import path
from . import views

urlpatterns = [
    path('', views.goto_index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),

]
