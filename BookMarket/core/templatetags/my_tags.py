import requests
from django import template

from cart.models import Cart

register = template.Library()


@register.inclusion_tag('core/top_cart_icon.html', takes_context=True)
def top_cart_icon(context):
    context['active'] = 'cart'

    cart_id = context['request'].session.get('cart_id')
    if cart_id:
        cart = Cart.objects.get(pk=int(cart_id))
        products = cart.products.all().count()
    else:
        products = 0
    return {
        'products': products
    }


@register.inclusion_tag('core/exchange_rates.html', takes_context=True)
def exchange_rates(context):
    r = requests.get('http://www.nbrb.by/API/ExRates/Rates/145')
    data = r.json()
    cur_abbr = data['Cur_Abbreviation']
    cur_rate = data['Cur_OfficialRate']
    context['rate'] = '1 ' + cur_abbr + ': ' + str(cur_rate) + ' BYN'
    return context


@register.filter('has_group')
def has_group(user, group_name):
    groups = user.groups.all().values_list('name', flat=True)
    return True if group_name in groups else False
