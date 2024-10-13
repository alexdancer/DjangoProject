from django.test import TestCase
from restaurant.models import Menu
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.serializers import MenuSerializer
from django.urls import reverse

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title='Pizza', price=10, inventory=100)
        self.menu2 = Menu.objects.create(title='Burger', price=8, inventory=75)
        self.menu3 = Menu.objects.create(title='Pasta', price=12, inventory=20)
    
    def test_getall(self):
        response = self.client.get(reverse('menu-items'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)