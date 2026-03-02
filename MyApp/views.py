from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404

from MyApp.models import Project, Task


# Create your views here.
def index(request):
    title = "Bienvenido a DJango App"
    return render(request, 'index.html', {
        'title': title
    })

def hello(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.<h1>")

def projects(request):
    projects_list = list(Project.objects.values())
    return JsonResponse(projects_list, safe=False)

def task(request, id_task):
    task_found = get_object_or_404(Task, id=id_task)
    return HttpResponse("<h2>Task: %s</h2>" % task_found.title)

def tasks(request):
    tasks_list = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks_list': tasks_list
    })