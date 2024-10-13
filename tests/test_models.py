from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_menu(self):
        menu = Menu.objects.create(title='Pizza', price=10, inventory=100)
        self.assertEqual(str(menu), "Pizza : 10")