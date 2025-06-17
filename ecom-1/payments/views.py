from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

class PaymentView(View):
    def get(self, request):
        return render(request, 'payments/payment_form.html')

    def post(self, request):
        amount = request.POST.get('amount')
        currency = 'usd'  # Change as needed

        try:
            # Create a new charge
            charge = stripe.Charge.create(
                amount=int(amount) * 100,  # Amount in cents
                currency=currency,
                source=request.POST['stripeToken'],
                description='Payment for course'
            )
            return redirect('payment_success')
        except stripe.error.StripeError:
            return redirect('payment_failure')

def payment_success(request):
    return render(request, 'payments/payment_success.html')

def payment_failure(request):
    return render(request, 'payments/payment_failure.html')