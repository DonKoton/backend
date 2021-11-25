from datetime import datetime
from django.shortcuts import render

# Create your views here.

def index(request):

    now = datetime.now()

    day = now.strftime('%w')
    is_it_monday = False

    if day == 1:
        is_it_monday = True


    return render(
        request,
        'isitmonday/index.html',
        context={
            'is_it_monday': is_it_monday
        }
    )
