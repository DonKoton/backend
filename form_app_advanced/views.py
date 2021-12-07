from django.shortcuts import render
from django.shortcuts import redirect

from form_app_advanced.models import Message

from form_app_advanced.forms import ContactForm

# Create your views here.

def contact1(request):
    if request.method == "POST":
        data = request.POST

        Message.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            category=data.get('category'),
            subject=data.get('subject'),
            body=data.get('body'),
            date=data.get('date'),
            time=data.get('time'),
        )

        return redirect('form_app_advanced:contact1')

    return render(
        request,
        'form_app_advanced/form_1.html',

    )


# formularz Django
def contact2(request):
    if request.method == "POST":
        print(request.POST)

    form = ContactForm()

    return render(
        request,
        'form_app_advanced/form_2.html',
        context={
            'form': form,

        }
    )
