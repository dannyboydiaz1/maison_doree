from django.urls import path
from .import views


urlpatterns = [
    path("", views.index, name="index"),
    # path("maison-templatemo/", views.maison_templatemo, name="maison-templatemo"),
]