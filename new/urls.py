from django.urls import path

from new import views

urlpatterns = [
    path('', views.layout, name='layout'),
    path('home/', views.home, name='home'),
    path('second/', views.second, name='second'),
    path('third/', views.third, name='third'),

]