from django.shortcuts import render
from django.shortcuts import redirect

TASKS = []

# Create your views here.

def register(request):

    return render(
        request,
        "form_app4/register.html",
    )


def tasks_list(request):
    if request.method == "POST":
        task = request.POST.get('task')
        if task:
            # TASKS.append(task)
            with open('tasks.txt', 'a+') as file:
                file.write(task + '\n')

        return redirect("form_app4:tasks_list")

    with open('tasks.txt', 'r') as file:
        tasks = file.readlines()

    return render(
        request,
        "form_app4/tasks_list.html",
        context={
            'tasks': tasks
        }
    )
