#coding: utf-8

from subscription.forms import SubscriptionForm
from subscription.models import Subscription
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.core.mail import send_mail


def new(request):
    form = SubscriptionForm(initial={
        'name': "Escreva seu nome",
        'cpf': 'Digite o seu CPF sem pontos',
        'email': "Escreva seu email",
        'phone_0': "Qual seu DDD",            
        'phone_1': "Qual seu telefone de contato",            
    })
    context = RequestContext(request, {'form': form})
    return render_to_response('subscription/new.html', context)

def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        context = RequestContext(request, {'form': form})
        return render_to_response('subscription/new.html', context)
    
    subscription = form.save()
    send_mail(
        subject = u'Inscrição no Eventex',
        message = u'Obrigado por se inscrever',
        from_email = 'thiagogds14@gmail.com',
        recipient_list = [ 'thiagogds@msn.com'],
    )
    return HttpResponseRedirect(reverse('subscription:success', args=[ subscription.pk]))

def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def success(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    context = RequestContext(request, { 'subscription': subscription })
    return render_to_response('subscription/success.html', context)
    
