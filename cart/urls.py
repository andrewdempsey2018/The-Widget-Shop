from django.urls import path

from . import views

urlpatterns = [
    path("add/<id>/", views.add, name='add'),
]