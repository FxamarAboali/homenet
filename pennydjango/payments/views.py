from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.db import transaction
from django.db.models import Sum

import stripe

from penny.mixins import ClientOrAgentRequiredMixin
from penny.models import User
from payments.models import Transaction
from leases.models import Lease, LeaseMember


class PaymentPage(ClientOrAgentRequiredMixin, TemplateView):
    def __init__(self):
        stripe.api_key = settings.STRIPE_PUBLISHABLE_KEY

    template_name = 'payments/payments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = stripe.api_key
        return context

    def post(self, request, *args, **kwargs):
        lease = get_object_or_404(Lease, id=kwargs.get('pk'))
        lease_cost = lease.moveincost_set.aggregate(Sum('value'))
        lease_cost = lease_cost['value__sum']
        client = LeaseMember.objects.get(user=request.user)
        cost_for_stripe = int(lease_cost *100)
        token = request.POST['stripeToken']

        try:
            stripe.Charge.create(
                amount=cost_for_stripe,
                currency='usd',
                description='A test charge',
                source=token,
                statement_descriptor='Custom descriptor'
            )
            
            with transaction.atomic(): 
                Transaction.objects.create(
                    service = lease,
                    made_by = request.user,
                    token = token,
                    amount = lease_cost
                )
            messages.success(request, 'Your payment was successfull')
            
        except stripe.error.CardError as e:
            message.info(request, "There has been a problem with your card")
        return HttpResponseRedirect(reverse('leases:detail-client', args=[client.id]))
        
