from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login_view(request):

    if request.method == "POST":
        data = request.POST

        user = authenticate(
            username=data.get('user'),
            password=data.get('password')
        )

        if user:
            login(request, user=user)

        return redirect('authentication:home')

    return render(
        request,
        'authentication/login.html',

    )


def home(request):
    if request.method == "POST":
        logout(request)

        return redirect('authentication:home')

    return render(
        request,
        'authentication/home.html',

    )


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('authentication:login_view')

    form = UserCreationForm()

    return render(
        request,
        'authentication/register.html',
        context={
            'form': form
        }
    )
