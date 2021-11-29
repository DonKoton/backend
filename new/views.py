from django.shortcuts import render

# Create your views here.

def layout(request):
    return render(
        request,
        'new/layout.html'
    )


def home(request):
    return render(
        request,
        'new/home.html'
    )


def second(request):
    return render(
        request,
        'new/second.html'
    )


def third(request):
    return render(
        request,
        'new/third.html'
    )


