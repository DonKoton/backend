from django.shortcuts import render
from django.shortcuts import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

# Create your views here.
def cookies(request):
    print(request.COOKIES)
    res = HttpResponse("OK")
    res.set_cookie('title', 'Bosh')
    res.set_cookie('ciasteczko2', 10, max_age=10)

    return res


def session(request):
    # print(dir(request.session))
    # print(request.session.session_key)
    session_id = request.session._get_or_create_session_key()
    res = HttpResponse("OK")
    res.set_cookie("sessionid", session_id)

    num_visit = request.session.get('num_visit', 0) + 1
    request.session['num_visit'] = num_visit
    return HttpResponse(f"Liczba odwiedzin: {num_visit}")


def auth(request):
    users = User.objects.all()
    print(users)

    # tworzenie usera
    adam = User.objects.create_user('seba', password='tajne')  # tak można stworzyć usera, ale hasło trzeba hashować samodzielnie

    users = User.objects.all()
    print(users)

    # uwierzytelnianie usera
    authenticated_user = authenticate(username='seba', password='tajne')

    # logowanie usera
    if authenticated_user:
        login(request, user=authenticated_user)

    # wylogowanie usera
    logout(request)

    return render(
        request,
        'auth_app/home.html',

    )
