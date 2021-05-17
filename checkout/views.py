from django.shortcuts import render, redirect, reverse
from .forms import MakePaymentForm, OrderForm
from django.conf import settings
import stripe
from django.contrib import messages

stripe.api_key = settings.STRIPE_SECRET

def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.save()

            try:
                customer = stripe.Charge.create(
                amount = int(999),
                currency = "EUR",
                description = request.user.email,
                card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect('index')
            else:
                messages.error(request, "Error getting payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take payment with that card!")

        return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})