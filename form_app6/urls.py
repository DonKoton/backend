from django.urls import path

from form_app6 import views

app_name = "form_app6"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('tasks_list/', views.tasks_list, name='tasks_list'),
    path('update/<int:task_id>/', views.update, name='update'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
]