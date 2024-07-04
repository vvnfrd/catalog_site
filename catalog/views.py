from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from catalog.forms import ProductForm, VersionForm, ProductFormForModerator
from catalog.models import Product, Version
from django.views.generic.list import ListView

from catalog.services import get_cached_categories_for_product


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    permission_required = 'catalog.view_product'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product_info.html'

    def get_object(self, queryset=None):
        self.product = super().get_object(queryset)
        self.product.views_counter += 1
        self.product.save()
        return self.product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['categories'] = get_cached_categories_for_product(self.object.pk)
        return context_data


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.add_product'
    success_url = reverse_lazy('catalog:list')
    template_name = 'product_form.html'

    def form_valid(self, product):
        if product.is_valid():
            new_product = product.save()
            new_product.slug = new_product.name.lower().replace(' ', '-')
            new_product.author = self.request.user.email
            new_product.save()

        return super().form_valid(product)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_product'
    success_url = reverse_lazy('catalog:list')
    template_name = 'product_form.html'

    def get_form_class(self):
        user = self.request.user
        if user.email == self.object.author:
            # print(user, self.object.name)
            return ProductForm
        elif user.groups.filter(name='moderators').exists():
            return ProductFormForModerator
        else:
            # print(user.email, self.object.author)
            raise PermissionDenied()

    def get_success_url(self):
        return reverse('catalog:info', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            raise self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    # permission_required = 'catalog.delete_product'
    success_url = reverse_lazy('catalog:list')
    template_name = 'product_confirm_delete.html'

    def test_func(self):
        return self.request.user.is_superuser


def is_this_owner(user):
    return user.groups.filter(name__in=['owner']).exists()