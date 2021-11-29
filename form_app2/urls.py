from django.urls import path

from form_app2 import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('tasks_list/', views.tasks_list, name='tasks_list'),
]