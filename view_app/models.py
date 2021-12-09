from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} z {self.city} <{self.age}>"

    def get_absolute_url(self):  # instrukcja dla widoku generycznego gdzie ma przekierować, korzystnie,
        return reverse('view_app:create_person3')  # bo można to wykorzystać też dla innych widoków
