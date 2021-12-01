from django.urls import path

from form_app4 import views

app_name = "form_app4"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('tasks_list/', views.tasks_list, name='tasks_list'),
]