from django.db import models

# Create your models here.

class Message(models.Model):
    title = models.CharField(max_length=128)
    email = models.EmailField()
    body = models.TextField()
    category = models.CharField(max_length=128, null=True)  # null=True oznacza to samo co default=coś, migracja bez konfliktu
    added = models.DateTimeField(auto_now_add=True)  # pole w momencie stworzenia ma wpisywaną datę
    modified = models.DateTimeField(auto_now=True)  # pole w momencie modyfikacji ma wpisywaną datę
