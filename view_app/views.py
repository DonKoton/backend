from django.shortcuts import render
from django.shortcuts import HttpResponse

# widoki klasowe
from django.views import View
# widoki generyczne
from django.views.generic import TemplateView
from django.views.generic import DetailView

from view_app.models import Person
from django.shortcuts import get_object_or_404

# function-based view (widok funkcyjny)
def hello(request):
    return HttpResponse("Hello, world!")


# class-based view (widok klasowy)
class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello, world!")


# function-based
def template_hello(request):
    return render(
        request,
        'view_app/hello.html'
    )


# class-based
class HelloClassView(View):
    def get(self, request):
        return render(
            request,
            'view_app/hello.html'
        )


# generic view - (widok generyczny)
class HelloGenericView(TemplateView):
    template_name = 'view_app/hello.html'


# widok funkcyjny
def template2_hello(request):
    name = "admin"

    return render(
        request,
        'view_app/hello2.html',
        context={
            "name": name
        }
    )


# class-based
class HelloClassView2(View):
    def get(self, request):
        name = "admin"

        return render(
            request,
            'view_app/hello2.html',
            context={
                "name": name
            }
        )


# generic view - (widok generyczny)
class HelloGenericView2(TemplateView):
    template_name = 'view_app/hello2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "root"
        return context


# widok funkcyjny
def person_detail(request, id):
    person = get_object_or_404(Person, id=id)

    return render(
        request,
        'view_app/person_detail.html',
        context={
            "person": person
        }
    )


# widok klasowy
class PersonView(View):
    def get(self, request, id):
        person = get_object_or_404(Person, id=id)

        return render(
            request,
            'view_app/person_detail.html',
            context={
                "person": person
            }
        )


# widok generyczny
class PersonDetailView(DetailView):
    model = Person



