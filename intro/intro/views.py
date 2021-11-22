from django.shortcuts import HttpResponse

# w django widok to coś, co przyjmuje request i zwraca HttpResponse
def index(request):
    return HttpResponse("Hello world!")  # musi być obiekt HttpResponse, bo string nie ma metody get
