from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product
from django.views.generic.list import ListView


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_info.html'

    def get_object(self, queryset=None):
        self.product = super().get_object(queryset)
        self.product.views_counter += 1
        self.product.save()
        return self.product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'price', 'image', 'category')
    success_url = reverse_lazy('catalog:list')
    template_name = 'product_form.html'


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'price', 'image', 'category')
    success_url = reverse_lazy('products:catalog')
    template_name = 'product_form.html'

    def get_success_url(self):
        return reverse('info:catalog', args=(self.kwargs.get('pk')))


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products:catalog')
    template_name = 'product_confirm_delete.html'

# def product_list(request):
#     product_list = Product.objects.all()
#     context = {'product_list': product_list}
#     return render(request, 'product_list.html', context)

# def product_info(request, pk):
#     product = Product.objects.get(pk=pk)
#     context = {'product': product}
#     return render(request, 'product_info.html', context)
