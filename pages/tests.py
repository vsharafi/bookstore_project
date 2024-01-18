from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):


    def test_homepage_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_home_page_urlname(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_content(self):
       response = self.client.get('')
       self.assertContains(response, 'Home Page')
