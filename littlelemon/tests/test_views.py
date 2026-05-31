from decimal import Decimal

from django.test import TestCase
from rest_framework.test import APIClient

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient(HTTP_HOST='localhost')
        Menu.objects.create(Title='Greek Salad', Price=Decimal('12.99'), Inventory=25)
        Menu.objects.create(Title='Bruschetta', Price=Decimal('8.50'), Inventory=15)
        Menu.objects.create(Title='Lemon Dessert', Price=Decimal('6.25'), Inventory=30)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/items')
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
