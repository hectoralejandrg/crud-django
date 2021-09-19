from django.views.generic import ListView, CreateView, DetailView, DeleteView

from escuela.models import Escuela


class EscuelaGenericView(ListView):
    model = Escuela
    context_object_name = 'escuelas'


class EscuelaCreateView(CreateView):
    model = Escuela
    fields = '__all__'
    success_url = '/escuela/'


class EscuelaDetailView(DetailView):
    queryset = Escuela.objects.all()


class EscuelaDeleteView(DeleteView):
    model = Escuela
    success_url = '/escuela/'

