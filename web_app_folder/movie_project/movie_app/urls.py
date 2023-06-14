from django.urls import path
from movie_app import views
app_name = 'movie_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:mid>/', views.update, name='update'),
    path('delete/<int:mid>/', views.delete, name='delete')
]
