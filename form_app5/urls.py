from django.urls import path

from form_app5 import views

app_name = "form_app5"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('tasks_list/', views.tasks_list, name='tasks_list'),
]
