from django.urls import path

from view_app import views

app_name = "view_app"

urlpatterns = [
    path('hello/', views.hello, name="hello"),
    path('hello2/', views.HelloView.as_view(), name="hello2"),  # do widoków klasowych inaczej się odwołuje
    path('template/hello/', views.template_hello, name="template_hello"),
    path('template/hello2/', views.HelloClassView.as_view(), name="template_hello2"),
    path('template/hello3/', views.HelloGenericView.as_view(), name="template_hello3"),
    path('template2/hello/', views.template2_hello, name="template2_hello"),
    path('template2/hello2/', views.HelloClassView2.as_view(), name="template2_hello2"),
    path('template2/hello3/', views.HelloGenericView2.as_view(), name="template2_hello3"),
    path('person/<int:id>', views.person_detail, name='person_detail'),
    path('person2/<int:id>', views.PersonView.as_view(), name='person_detail2'),
    # dla widoku generycznego detalu (DetailView) zmienna w konwerterze funkcji path musi nazywać się pk !!!
    path('person3/<int:pk>', views.PersonDetailView.as_view(), name='person_detail3'),

]


