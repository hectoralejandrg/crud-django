from django.urls import path

from student.views import *

app_name = 'student'
urlpatterns = [
    path('', StudentGenericView.as_view(), name='list'),
    path('new', StudentCreateView.as_view(), name='new'),
    path('<pk>/', StudentDetailView.as_view(), name='detail'),
    path('delete/<pk>/', StudentDeleteView.as_view(), name='delete'),
    path('class/list', ClassGenericView.as_view(), name='list_class'),
    path('class/new', ClassCreateView.as_view(), name='new_class'),
    path('class/<pk>/', ClassDetailView.as_view(), name='detail_class'),
    path('class/delete/<pk>/', ClassDeleteView.as_view(), name='delete_class'),
]