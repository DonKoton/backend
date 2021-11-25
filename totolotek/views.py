import random
from django.shortcuts import render

# Create your views here.

def index(request):

    totolotto = random.sample(range(1, 49), 6)

    return render(
        request,
        'totolotek/first.html',
        context={
            'totolotto': totolotto
        }
    )