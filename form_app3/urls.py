from django.urls import path

from form_app3 import views

app_name = "form_app3"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('tasks_list/', views.tasks_list, name='tasks_list'),
]