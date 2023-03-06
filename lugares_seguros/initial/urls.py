from django.urls import path

from initial import views

urlpatterns = [
    path("", views.HelloDrf.as_view(), name="index")

]
