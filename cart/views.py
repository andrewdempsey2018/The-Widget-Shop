from django.shortcuts import render, redirect, reverse, get_object_or_404

from widget.models import Widget

def view_cart(request):
    cart = request.session.get('cart', {})
    total = 0

    for key, value in cart.items():
        total += int(value.get('quantity')) * int(value.get('price'))

    return render(request, "cart/view_cart.html", {'cart': cart, 'total': total})

def add_to_cart(request, id):
    cart = request.session.get('cart', {})
    product = get_object_or_404(Widget, pk=id)

    if id in cart.keys():
        val1 = int(cart[id].get('quantity'))
        val2 = int(request.POST['quantity'])
        val3 = val1+val2
        cart[id]['quantity'] = val3
    else:
        cart[id] = {'product_name': product.name, 'quantity': request.POST['quantity'], 'image': product.detailPicSmall, 'price': product.price}

    
    request.session['cart'] = cart
    return redirect('index')