from django.views.generic import DetailView, FormView, ListView, DeleteView, CreateView
from .models import Prf
from django.contrib.auth.models import User, Group
from django.urls import reverse, reverse_lazy
from .forms import PrflUpdateForm, RegisterForm
from cart.models import Cart
from products.models import Book
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class PrflDetailView(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login/'
    template_name = 'prfls/prfls_view.html'
    model = User

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def get_context_data(self, **kwargs):
        context = super(PrflDetailView, self).get_context_data(**kwargs)
        user = self.request.user
        user_order = {}
        quantity_product_in_order = []
        for order in Cart.objects.filter(user_id=user.pk):
            books = Book.objects.filter(product_in_cart__cart=order)
            my_dic = {order: books}
            user_order.update(my_dic)
        context['user_order'] = user_order
        context['quantity_product_in_order'] = quantity_product_in_order
        return context


class PrflUpdateView(LoginRequiredMixin, FormView):
    login_url = '/accounts/login/'
    template_name = 'prfls/prfls_update.html'
    model = User

    def get_success_url(self):
        return reverse('prfls:prfls-view')

    def get_form(self, form_class=None):
        user = self.request.user
        del_addr, created = Prf.objects.get_or_create(
            customer=user,
        )
        if self.request.method == 'POST':
            my_form = PrflUpdateForm(self.request.POST)
            user.username = my_form['username'].value()
            user.first_name = my_form['first_name'].value()
            user.last_name = my_form['last_name'].value()
            user.email = my_form['email'].value()
            us_addr = Prf.objects.get(customer_id=user.id)
            us_addr.delivery_address = my_form['delivery_address'].value()
            us_addr.phone_number = my_form['phone_number'].value()
            us_addr.save()
            user.save()
            return my_form
        else:
            my_form = PrflUpdateForm(
                initial={'delivery_address': user.prf.delivery_address,
                         'username': user.username,
                         'first_name': user.first_name,
                         'last_name': user.last_name,
                         'email': user.email,
                         'phone_number': user.prf.phone_number
                         }
            )
            return my_form


class PrflListView(ListView):
    model = User
    template_name = 'prfls/prfls_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        my_group = Group.objects.get(name='Customers')
        users = User.objects.filter(groups=my_group)
        context = {'users': users}
        return context


class PrflDetailForManagersView(PermissionRequiredMixin, DetailView):
    model = User
    template_name = 'prfls/prfls_view-for-managers.html'
    permission_required = 'prfs.view_prf'


class PrflUpdateForManagersView(PermissionRequiredMixin, PrflUpdateView):
    template_name = 'prfls/prfls_update.html'
    model = User
    permission_required = 'prfs.change_prf'

    def get_success_url(self):
        return reverse('prfls:prfls-view-for-managers', args=(self.kwargs['pk'],))

    def get_form(self, form_class=None):
        user = User.objects.get(id=self.kwargs['pk'])
        del_addr, created = Prf.objects.get_or_create(
            customer=user,
        )
        if self.request.method == 'POST':
            my_form = PrflUpdateForm(self.request.POST)
            user.username = my_form['username'].value()
            user.first_name = my_form['first_name'].value()
            user.last_name = my_form['last_name'].value()
            user.email = my_form['email'].value()
            us_addr = Prf.objects.get(customer_id=user.id)
            us_addr.delivery_address = my_form['delivery_address'].value()
            us_addr.phone_number = my_form['phone_number'].value()
            us_addr.save()
            user.save()
            return my_form
        else:
            my_form = PrflUpdateForm(
                initial={'delivery_address': user.prf.delivery_address,
                         'username': user.username,
                         'first_name': user.first_name,
                         'last_name': user.last_name,
                         'email': user.email,
                         'phone_number': user.prf.phone_number
                         }
            )
            return my_form


class PrflDeleteForManagersView(PermissionRequiredMixin, DeleteView):
    model = User
    template_name = 'prfls/prfls_delete-for-managers.html'
    success_url = reverse_lazy('prfls:prfls-list')
    permission_required = 'prfs.delete_prf'


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'prfls/register.html'
    success_url = reverse_lazy('Core')
