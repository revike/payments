import stripe
from django.http import HttpResponseRedirect, Http404
from django.views.generic import DetailView, TemplateView, ListView

from main_app.models import Item
from payments.settings import DOMAIN_NAME, STRIPE_SECRET_KEY, STRIPE_PUBLIC_KEY

stripe.api_key = STRIPE_SECRET_KEY


class ItemListView(ListView):
    """Controller for Items List"""
    template_name = 'main_app/products.html'
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'products'
        return context


class ItemDetailView(DetailView):
    """Controller fot Item Detail"""
    template_name = 'main_app/product.html'
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context


class BuyView(TemplateView):
    """Controller for buy"""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'STRIPE_PUBLIC_KEY': STRIPE_PUBLIC_KEY})
        return context

    def get(self, request, *args, **kwargs):
        product = Item.objects.filter(id=kwargs['pk']).first()
        if product:
            price = int(product.price * 100)
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'rub',
                            'unit_amount': price,
                            'product_data': {
                                'name': product.name,
                            }
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=f'{DOMAIN_NAME}/success/',
                cancel_url=f'{DOMAIN_NAME}/cancel/',
            )
            return HttpResponseRedirect(checkout_session.url)
        raise Http404


class SuccessView(TemplateView):
    """Controller success buy"""
    template_name = 'main_app/success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'success'
        return context


class CancelView(TemplateView):
    """Controller cansel buy"""
    template_name = 'main_app/cancel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'cansel'
        return context
