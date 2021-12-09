from django.urls import path

from authentication import views

app_name = "authentication"

urlpatterns = [
    path('login_view/', views.login_view, name="login_view"),
    path('home/', views.home, name="home"),
    path('register/', views.register, name="register"),
]