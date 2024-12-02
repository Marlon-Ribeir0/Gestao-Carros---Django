from carros.models import Carro
from carros.forms import carroModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

class CarrosListView(ListView):
    model = Carro
    template_name = 'carros.html'
    context_object_name = 'carros'

    def get_queryset(self):
        carros = super().get_queryset().order_by('marca')
        search = self.request.GET.get('search')
        if search:
            carros = Carro.objects.filter(modelo__icontains=search)
        return carros
    

class carroDetales(DetailView):
    model = Carro
    template_name = 'carro_detalhes.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class NovoCarroCreateView(CreateView):
    model = Carro
    form_class = carroModelForm
    template_name = 'novo_carro.html'
    success_url = '/carros/'


@method_decorator(login_required(login_url='carro_atualizar'), name='dispatch')
class carroAtualizar(UpdateView):
    model = Carro
    form_class = carroModelForm
    template_name = 'carro_atualizar.html'

    def get_success_url(self):
        return reverse_lazy('detalhes', kwargs={'pk': self.object.pk})
    

@method_decorator(login_required(login_url='carro_apagar'), name='dispatch')
class carroApagar(DeleteView):
    model = Carro
    template_name = 'carro_deleta.html'
    success_url = '/carros/'