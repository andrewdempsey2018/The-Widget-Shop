from django.urls import path

from . import views

urlpatterns = [
    path("add/<id>/", views.add, name='add'),
    path("view_cart/", views.view_cart, name='view_cart'),
    path("add_to_cart/<id>/", views.add_to_cart, name='add_to_cart'),
]