from django.urls import path

from clase.views import ClaseGenericView,ClaseCreateView,ClaseDetailView,ClaseDeleteView

app_name = 'clase'
urlpatterns = [
    path('', ClaseGenericView.as_view(), name='list_clase'),
    path('new', ClaseCreateView.as_view(), name='new_clase'),
    path('<pk>/', ClaseDetailView.as_view(), name='detail_clase'),
    path('delete/<pk>/', ClaseDeleteView.as_view(), name='delete_clase'),
]