from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import CarModel


class CarTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        credentials = {"username": "test_username", "password": "test_password"}
        cls.user = User.objects.create_user(**credentials)

    def setUp(self) -> None:
        self.client.force_authenticate(user=self.user)

    def test_create_car(self):
        url = reverse("car-list")
        data = {"name": "car1", "model": 1}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created = CarModel.objects.get()
        self.assertEqual(CarModel.objects.count(), 1)
        self.assertEqual(created.name, data["name"])
        self.assertEqual(created.model, data["model"])
