from django.views.generic import CreateView, DetailView, DeleteView,ListView

from clase.models import Clase


class ClaseGenericView(ListView):
    model = Clase
    context_object_name = 'clases'


class ClaseCreateView(CreateView):
    model = Clase
    fields = '__all__'
    success_url = '/clase/'


class ClaseDetailView(DetailView):
    queryset = Clase.objects.all()


class ClaseDeleteView(DeleteView):
    model = Clase
    success_url = '/clase/'

