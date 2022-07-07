from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.NotebookCreateView.as_view(), name='create'),
    path('all/', views.NotebookListView.as_view(), name='all_records'),
    path('update/<int:pk>', views.NotebookUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.NotebookDeleteView.as_view(), name='delete'),
    path('task/<int:pk>', views.NotebookTaskView.as_view(), name='task'),

]
