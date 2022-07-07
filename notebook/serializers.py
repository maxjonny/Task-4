
from rest_framework import serializers
from .models import Notebook


class NotebookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebook
        fields = ('__all__')


class NotebookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebook
        fields = ('header', 'description', 'date_of_completion')


class NotebookStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebook
        fields = ('status',)

