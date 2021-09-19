from django.urls import path

from escuela.views import *

app_name = 'escuela'
urlpatterns = [
    path('', EscuelaGenericView.as_view(), name='list_escuela'),
    path('new', EscuelaCreateView.as_view(), name='new_escuela'),
    path('<pk>/', EscuelaDetailView.as_view(), name='detail_escuela'),
    path('delete/<pk>/', EscuelaDeleteView.as_view(), name='delete_escuela'),
]