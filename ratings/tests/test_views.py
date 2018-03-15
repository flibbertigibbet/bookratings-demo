from django.test import Client, TestCase


class IndexViewTextCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page_redirects_when_no_cookie(self):
        response = self.client.get('')
        self.assertRedirects(
            response, '/signup/', status_code=302, target_status_code=200)

    def test_index_page_recognizes_cookie(self):
        pass
