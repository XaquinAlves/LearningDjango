from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('projects/', views.projects),
    path('task/<int:id_task>/', views.task),
    path('tasks/', views.tasks),
]
