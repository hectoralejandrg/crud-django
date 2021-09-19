from django.urls import path

from student.views import *

app_name = 'student'
urlpatterns = [
    path('', StudentGenericView.as_view(), name='list'),
    path('new', StudentCreateView.as_view(), name='new'),
    path('<pk>/', StudentDetailView.as_view(), name='detail'),
    path('delete/<pk>/', StudentDeleteView.as_view(), name='delete'),
]