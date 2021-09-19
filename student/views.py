from django.views.generic import ListView, CreateView, DetailView, DeleteView

from student.models import Student


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

