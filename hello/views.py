from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_view(request):
    text = """
    <!DOCTYPE html>
    <head>
        <title>
            Hello
        </title>
    </head>
    <body>
        <h1>
            Hello, world!
        </h1>
    </body>
    </html>
    """
    return HttpResponse(text)


def hello2_view(request):
    return render(request, 'hello.html')


def adam_view(request):
    return HttpResponse('Witaj, Adam!')


def ewa_view(request):
    return HttpResponse('Witaj, Ewa!')


def name_view(request, name):  # tu musi być taka sama zmienna jak w endpoincie w urls.py
    from markupsafe import escape  # moduł do oczyszczania wprowadzanych danych
    name = name.title()
    return HttpResponse(f'Witaj, {escape(name)}!')


def name_view2(request, name):  # funkcja do zabezpieczania przed wstrzykiwaniem kodu w urlu
    return render(
            request,
            'name.html',
            context={
                'name_in_template': name
            }
    )