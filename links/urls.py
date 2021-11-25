from django.urls import path

from links import views

app_name = 'links'

urlpatterns = [
    path('first/', views.first, name="first"),  # dynamicznie linkowanie
    path('second/', views.second, name="second"),
    path('third/<str:value>/', views.third, name="third"),
]