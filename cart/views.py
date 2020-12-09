from django.shortcuts import render, redirect, reverse, get_object_or_404

from widget.models import Widget

def add(request, id):
    cart = request.session.get('cart', {})
    cart['vagekey'] = get_object_or_404(Widget, pk=id)

    request.session['cart'] = cart
    return redirect(reverse('index'))

def view_cart(request):
    cart = request.session.get('cart', {})
    return render(request, "cart/view_cart.html", {'cart': cart})

def add_to_cart(request, id):
    cart = request.session.get('cart', {})
    product = get_object_or_404(Widget, pk=id)
    cart[id] = {'product_name': product.name, 'quantity': request.POST['quantity'], 'image': product.detailPicSmall}
    request.session['cart'] = cart
    return redirect('index')