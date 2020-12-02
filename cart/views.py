from django.shortcuts import render, redirect, reverse

def add(request, id):
    cart = request.session.get('cart', {})
    #cart[len(cart)] = 'asd'

    request.session['cart'] = cart
    return redirect(reverse('index'))

def view_cart(request):
    cart = request.session.get('cart', {})
    return render(request, "cart/view_cart.html", {'cart': cart})