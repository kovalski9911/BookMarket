from django.urls import reverse_lazy
from django.views.generic import UpdateView, TemplateView, DeleteView

from orders.forms import OrderForm
from prfs.models import Prf
from products.models import Book
from reference.models import OrderStatus
from .forms import AddToCartForm
from .models import ProductsInCart, Cart


class AddProductCartView(UpdateView):
    template_name = 'cart/add_to_cart.html'
    form_class = AddToCartForm
    model = ProductsInCart
    success_url = reverse_lazy('cart:view')

    def get_object(self, queryset=None):
        cart_id = self.request.session.get('cart_id')
        product_id = self.kwargs.get('product')
        usr = None
        if self.request.user.is_authenticated:
            usr = self.request.user
        cart, cart_created = Cart.objects.get_or_create(
            pk=cart_id,
            defaults={
                'user': usr
            }
        )
        product = Book.objects.get(pk=product_id)
        product_in_cart, product_in_cart_created = ProductsInCart.objects.get_or_create(
            cart=cart,
            book=product,
            defaults={
                'cart': cart,
                'book': product,
                'quantity': 1
            }
        )
        if cart_created:
            self.request.session['cart_id'] = cart.pk
        elif not product_in_cart_created:
            product_in_cart.quantity += 1
        return product_in_cart


class ListCartView(TemplateView):
    template_name = 'cart/view_cart.html'
    model = Cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cart_id = self.request.session.get('cart_id')
        usr = None
        if self.request.user.is_authenticated:
            usr = self.request.user
        cart, cart_created = Cart.objects.get_or_create(
            pk=cart_id,
            defaults={
                'user': usr
            }
        )
        if cart_created:
            self.request.session['cart_id'] = cart.pk

        prod_in_cart = ProductsInCart.objects.filter(cart__pk=cart_id)
        context['prod_in_cart'] = prod_in_cart
        if len(prod_in_cart) == 0:
            context['empty'] = 'Ваша корзина пуста'

        cnt = 0
        for product in ProductsInCart.objects.filter(cart__pk=cart_id):
            cnt += product.quantity
        context['product_count'] = cnt

        tot_pr = 0
        for product in ProductsInCart.objects.filter(cart__pk=cart_id):
            tot_pr += product.quantity * product.book.price
        context['total_price'] = tot_pr

        order_status, created = OrderStatus.objects.get_or_create(
            name='В обработке',
            description='Зака находится в обработке'
        )

        # добавить проверку на зарегестрированного юзера
        us_prfl = Prf.objects.get(customer_id=usr.id)
        data = {'cart': cart,
                'status': order_status,
                'phone': us_prfl.phone_number,
                'email': usr.email,
                'delivery_address': us_prfl.delivery_address
                }
        context['order_form'] = OrderForm(initial=data)

        return context


class UpdateProductCartView(UpdateView):
    template_name = 'cart/add_to_cart.html'
    form_class = AddToCartForm
    model = ProductsInCart
    success_url = reverse_lazy('cart:view')


class DeleteProductCartView(DeleteView):
    form_class = AddToCartForm
    template_name = 'cart/delete_from_cart.html'
    success_url = reverse_lazy('cart:view')
    model = ProductsInCart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['prod_action'] = 'Удалить выбранный товар из корзины'

        return context
