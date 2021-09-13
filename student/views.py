from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, DetailView, DeleteView

from student.models import Student, Class


class StudentGenericView(ListView):
    model = Student
    context_object_name = 'students'


class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    success_url = '/student/'


class StudentDetailView(DetailView):
    queryset = Student.objects.all()


class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/student/'


class ClassGenericView(ListView):
    model = Class
    context_object_name = 'classes'


class ClassCreateView(CreateView):
    model = Class
    fields = '__all__'
    success_url = '/student/class/list'


class ClassDetailView(DetailView):
    queryset = Class.objects.all()


class ClassDeleteView(DeleteView):
    model = Class
    success_url = '/student/class/list'

