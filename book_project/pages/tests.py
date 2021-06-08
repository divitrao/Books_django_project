from django.test import TestCase , SimpleTestCase

from django.urls  import reverse, resolve
from .views import HomePage
class Homepagetest(SimpleTestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_homepge_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    def test_homepage_html(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response,'home.html')

    def test_homepage_contains_correct_html(self):  # new
        response = self.client.get(reverse('home'))

        self.assertContains(response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):  # new
        response = self.client.get('/')

        self.assertNotContains(response, 'Hi there! I should not be on the page.')

    def test_home_url_resolve(self):
        response = self.client.get(reverse('home'))
        view = resolve('/')
        self.assertEqual(view.func.__name__,HomePage.as_view().__name__)
