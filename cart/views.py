from django.shortcuts import render, redirect, reverse

# Create your views here.
#def add(request, id):
#    quantity = 0

#    cart = request.session.get('cart', {})
#    cart[id] = cart.get(id, quantity)

#    request.session['cart'] = cart
#    return redirect(reverse('index'))

# Create your views here.
def add(request, id):
    cart = request.session.get('cart', {})
    cart[len(cart)] = 'asd'

    request.session['cart'] = cart
    return redirect(reverse('index'))

def view(request):
    cart = request.session.get('cart', {})
    return render(request, "cart/view.html", {'cart': cart})