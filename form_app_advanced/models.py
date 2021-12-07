from django.db import models

# Create your models here.
class Message(models.Model):
    CHOICES = [
        ("question", "Pytanie"),
        ("other", "Inne"),
    ]


    name = models.CharField(max_length=128)
    email = models.EmailField()
    category = models.CharField(max_length=16, choices=CHOICES)  # dodawanie tych rzeczy pozwala się zabezpieczyć na poziomie Django
    subject = models.CharField(max_length=128)  # gdyby próbować robić niewłaściwe wpisy na poziomie bazy danych, to wszystko jest możliwe
    body = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    added = models.DateTimeField(auto_now_add=True)  # domyślnie data dodania wpisu
    modified = models.DateTimeField(auto_now=True)  # domyślnie data modyfikacja wpisu


    def __str__(self):
        return self.name