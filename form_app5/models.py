from django.db import models

# Create your models here.
class Task(models.Model):   # pierwszy krok do ORM - stworzenie klasy bazowej
    text = models.TextField()

    def __str__(self):
        return f"{self.text}"
