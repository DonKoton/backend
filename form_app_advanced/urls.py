from django.urls import path

from form_app_advanced import views

app_name = 'form_app_advanced'

urlpatterns = [
    path('contact1/', views.contact1, name='contact1'),
    path('contact2/', views.contact2, name='contact2'),
]