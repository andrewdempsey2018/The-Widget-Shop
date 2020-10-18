from django.urls import path

from . import views

urlpatterns = [
    path("detail/<slug>/", views.detail, name='detail'),
]