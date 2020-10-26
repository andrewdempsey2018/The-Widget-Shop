from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add(request, honk):
    print("Cart says Hello")
    print(honk)
    request.session[honk] = "1234"
    return render(request, "cart/thanks.html")