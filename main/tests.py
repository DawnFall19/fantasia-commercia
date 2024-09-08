from django.test import TestCase, Client
from django.utils import timezone
from .models import ItemEntry

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_rarity_of_item(self):
        now = timezone.now()
        item = ItemEntry.objects.create(
          name = "Huge Intelligence Potion",
          access_time = now,
          description = "Intelligence +10",
          price = 10000000,
          rarity = 4,
        )
        self.assertTrue(item.is_rare())