from django.test import Client, TestCase


class IndexViewTextCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page_renders(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
