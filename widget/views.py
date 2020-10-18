from django.shortcuts import render
from django.http import HttpResponse

from .models import Widget

#def detail(request):
#    return render(request, "widget/detail.html")

def detail(request, slug):
    widget = Widget.objects.get(slug=slug)
    return render(request, "widget/detail.html", {'widget':widget})
