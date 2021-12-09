from django.urls import path

from auth_app import views

app_name = "auth_app"

urlpatterns = [
    path('cookies/', views.cookies, name="cookies"),
    path('session/', views.session, name="session"),
    path('auth/', views.auth, name="auth"),
]