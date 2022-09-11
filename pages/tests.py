from pydoc import resolve
from urllib import response
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView

class HomepageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTrue(self.response, 'home.html')
    
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Home page')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "cold beans aint hot bro")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

class AboutpageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_about_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_page_template(self):
        self.assertTrue(self.response, 'about.html')
    
    def test_about_page_contains_correct_html(self):
        self.assertContains(self.response, 'About page')

    def test_about_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "cold beans aint hot bro")

    def test_about_page_url_resolves_about_pageview(self):
        view = resolve('/about')
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
