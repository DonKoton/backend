# plik do tworzenia formularzy, ułatwianie sprawy, żeby nie trzeba było tak bardzo korzystać z HTMLa

from django import forms
from django.forms.widgets import NumberInput


class ContactForm(forms.Form):
    CHOICES = [
        ("question", "Pytanie"),
        ("other", "Inne"),
    ]

    name = forms.CharField(label="Imię")
    email = forms.EmailField(label="Email")
    category = forms.ChoiceField(choices=CHOICES, label="Kategoria")
    subject = forms.CharField(label="Temat")
    body = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 40}), label="Treść")  # pola formularza mają domyślne widżety, ale można je nadpisać
    date = forms.DateField(widget=NumberInput(attrs={"type": "date"}), label="Ulubiona data")  # widżety daty i czasu trzeba oddzielnie zaimportować
    time = forms.TimeField(widget=NumberInput(attrs={"type": "time"}), label="Ulubiona godzina")