from django.contrib import admin
from view_app.models import Person

# Register your models here.
# admin.site.register(Person)

# reprezentacja modelu w panelu admina
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "city")
