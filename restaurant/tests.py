from django.test import TestCase
from .models import MenuItem

# Create your tests here.


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(name="test_name", price=45, description="This is a test menu item")
        self.assertEqual(item.name, "test_name")
