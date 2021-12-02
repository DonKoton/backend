# na start - zainicjować projekt django:
# django-admin startproject <name>
# tworzy się nowy folder

# dalej - python manage.py - wyświetla listę dostępnych komend

# python manage.py runserver - ta komenda uruchamia serwer django

# dalej - python manage.py startapp <name> - rozpoczęcie tworzenia nowej aplikacji
# w pliku settings.py trzeba wpisać nazwę utworzonego folderu do listy INSTALLED_APPS
# w pliku urls.py (w folderze intro) trzeba stworzyć wpis w globalnym dyspozytorze url
# stworzyć plik urls.py w lokalnym dyspozytorze url (w folderze aplikacji)
# w pliku views.py (hello) trzeba stworzyć widok (funkcję)

### DEBUG = True - serwer deweloperski
### DEBUG = False - serwer produkcyjny

# dalej - stworzyć folder templates i tam umieścić folder w formie szufladki, o nazwie takiej jak nazwa aplikacji, i w nim szablony - pliki html
# dalej - stworzyć folder static i tam umieszczać foldery css i js z odpowiednimi plikami i w folderze static umieszczać obrazki i inne pliki statyczne



# ORM - SQL
# migracje - 2 kroki:
# 1. makemigrations
# 2. migrate