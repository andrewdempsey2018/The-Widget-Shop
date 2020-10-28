from django.shortcuts import get_object_or_404

from widget.models import Widget

def cart_contents(request):
    """
    comment
    """


    cart = request.session.get('cart', {})
    cart_items = []

    total = 0
    product_count = 0

    for id, quantity in cart.items():
        widget = get_object_or_404(Widget, pk=id)
        total = 0
        product_count = 0
        cart_items.append({'id': id, 'quantity': quantity, 'widget': widget})
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}