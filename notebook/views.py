

from rest_framework import generics
from .serializers import *
from .models import Notebook


class NotebookCreateView(generics.CreateAPIView):
    serializer_class = NotebookCreateSerializer


class NotebookListView(generics.ListAPIView):
    queryset = Notebook.objects.all()
    serializer_class = NotebookDetailSerializer


class NotebookUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Notebook.objects.all()
    serializer_class = NotebookStatusSerializer


class NotebookDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Notebook.objects.all()
    serializer_class = NotebookDetailSerializer


class NotebookTaskView(generics.RetrieveAPIView):
    queryset = Notebook.objects.all()
    serializer_class = NotebookDetailSerializer
