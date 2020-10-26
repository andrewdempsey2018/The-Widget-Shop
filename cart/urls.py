from django.urls import path

from . import views

urlpatterns = [
    path("add/<honk>/", views.add, name='add'),
]