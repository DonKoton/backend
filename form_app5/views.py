from django.shortcuts import render
from django.shortcuts import redirect
from form_app5.models import Task

# Create your views here.

def register(request):
    tasks = []

    return render(
        request,
        'form_app5/register.html',
        context={
            'tasks': tasks
        }
    )


def tasks_list(request):

    task = request.POST.get('task')

    with open('tasks.txt', 'a+') as file:
        if task:
            # CREATE
            Task.objects.create(text=task)  # tworzenie do bazy danych

            # file.write(task + "\n")  # tworzenie do pliku
            # return redirect('form_app5:tasks_list')

    # READ
    tasks = Task.objects.all()  # wczytywanie z bazy danych

    # with open('tasks.txt', 'r') as file:  # wczytywanie z pliku do listy
    #     tasks = file.readlines()

    return render(
        request,
        'form_app5/tasks_list.html',
        context={
            'tasks': tasks
        }
    )