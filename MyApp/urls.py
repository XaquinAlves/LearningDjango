from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('projects/', views.projects, name='projects'),
    path('task/<int:id_task>/', views.task, name='task'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/new/', views.create_task, name='create_task')
]
