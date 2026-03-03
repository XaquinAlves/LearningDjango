import django.views.defaults
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from MyApp.models import Project, Task
from MyApp.forms import CreateNewTask


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

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': CreateNewTask()
        })
    elif request.method == 'POST':
        new_task = Task.objects.create(title=request.POST['title'], description=request.POST['description'],  project_id=1)
        new_task.save()
        return redirect('tasks')
    else:
        return HttpResponse("<h1>405 Method Not Allowed.<h1>",
                            status=405)
