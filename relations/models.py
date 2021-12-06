from django.db import models

# Create your models here.


# one-to-one
class Capital(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=128)
    capital = models.OneToOneField('Capital', on_delete=models.CASCADE) # 2 parametry obowiązkowe, przy usunięciu któregoś wpisu w jednej tabeli, w drugiej też jest usuwany powiązany wpis

    def __str__(self):
        return self.name

# one-to-many
class Language(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=128)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# many-to-many
class Movie(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=128)
    movies = models.ManyToManyField(Movie)  # on_delete nieobowiązkowy

    def __str__(self):
        return self.name