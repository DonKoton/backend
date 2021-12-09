from django import forms

from view_app.models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
