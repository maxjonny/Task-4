
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Notebook
from django.urls import reverse
from django.utils import timezone as tz
from .serializers import NotebookDetailSerializer

class NotebookTest(APITestCase):

	def setUp(self):
		self.record = Notebook.objects.create(
			header='test1',
			description='text',
			date_of_completion=tz.now().date()
		)

	def test_ListView(self):
		response = self.client.get(reverse('all_records'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)

	def test_CreateView(self):
		params = {"header": "ololo", "description": "123", "date_of_completion": "2020-01-01"}
		response = self.client.post(reverse('create'), params)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_UpdateView(self):
		params = {"status": 1}
		response = self.client.put(reverse('update', kwargs={"pk": 1}), params)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_TaskView(self):
		response = self.client.get(reverse('task', kwargs={"pk": 1}))
		serializer_data = NotebookDetailSerializer(self.record).data
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data, serializer_data)

	def test_DeleteView(self):
		response = self.client.delete(reverse('delete', kwargs={"pk": 1}))
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

	def test_invalid_header(self):
		params = {"header": "test1", "description": "123", "date_of_completion": "2020-01-01"}
		response = self.client.post(reverse('create'), params)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
