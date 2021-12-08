from django.shortcuts import render
from django.shortcuts import redirect

from form_app_advanced.models import Message

from form_app_advanced.forms import ContactForm

from form_app_advanced.forms import MessageForm

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


# formularz Django - automatyczne tworzenie HTMLa i automatyczna walidacja
def contact2(request):
    if request.method == "POST":
        form = ContactForm(request.POST)  # bound - formularz związany
        if form.is_valid():
            data = form.cleaned_data

            Message.objects.create(
                name=data.get("name"),
                email=data.get("email"),
                category=data.get("category"),
                subject=data.get("subject"),
                body=data.get("body"),
                date=data.get("date"),
                time=data.get("time"),
            )

            return redirect('form_app_advanced:contact2')


    form = ContactForm()  # unbound - formularz niezwiązany

    return render(
        request,
        'form_app_advanced/form_2.html',
        context={
            'form': form,

        }
    )


# formularze modelu Django
def contact3(request):

    if request.method == "POST":
        form = MessageForm(request.POST)
        form.save()


        return redirect('form_app_advanced:contact3')

    form = MessageForm()

    return render(
        request,
        'form_app_advanced/form_3.html',
        context={
            "form": form
        }
    )




