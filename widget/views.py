from django.shortcuts import render
from django.http import HttpResponse

def detail(request):
    return render(request, "widget/detail.html")
