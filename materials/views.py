from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from materials.models import Material
from django.views.generic.list import ListView


class MaterialListView(ListView):
    model = Material
    # fields = ('title', 'body', 'image', 'create_at')
    template_name = 'material_list.html'


class MaterialDetailView(DetailView):
    model = Material
    template_name = 'material_info.html'

    def get_object(self, queryset=None):
        self.material = super().get_object(queryset)
        self.material.views_counter += 1
        self.material.save()
        return self.material


class MaterialCreateView(CreateView):
    model = Material
    fields = ('title', 'body', 'image')
    success_url = reverse_lazy('materials:list')
    template_name = 'material_form.html'


class MaterialUpdateView(UpdateView):
    model = Material
    fields = ('title', 'body', 'image')
    success_url = reverse_lazy('materials:list')
    template_name = 'material_form.html'

    def get_success_url(self):
        return reverse('materials:info', args=(self.kwargs.get('pk')))


class MaterialDeleteView(DeleteView):
    model = Material
    success_url = reverse_lazy('material:materials')
    template_name = 'material_confirm_delete.html'

# def product_list(request):
#     product_list = Product.objects.all()
#     context = {'product_list': product_list}
#     return render(request, 'product_list.html', context)

# def product_info(request, pk):
#     product = Product.objects.get(pk=pk)
#     context = {'product': product}
#     return render(request, 'product_info.html', context)
