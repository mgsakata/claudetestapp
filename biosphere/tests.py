from django.test import TestCase
from django.urls import reverse


class BiosphereViewTests(TestCase):
    def test_index_status_ok(self):
        response = self.client.get(reverse('biosphere:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_uses_template(self):
        response = self.client.get(reverse('biosphere:index'))
        self.assertTemplateUsed(response, 'biosphere/index.html')
