from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('add_task/', views.add_todo, name='add_todo'),
    path('delete_task/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path("change/<int:task_id>/", views.change, name='change'),
]
