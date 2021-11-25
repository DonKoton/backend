from django.urls import path

from totolotek import views

urlpatterns = [
    path('', views.index)
]