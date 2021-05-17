from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', include("widget.urls")),
    path('', include("cart.urls")),
    path('', include("checkout.urls")),
]
