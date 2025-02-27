from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class TestPages(SimpleTestCase):
    def test_url_exists_at_correct_location_home_page_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
