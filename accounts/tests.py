from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class SignUpTest(TestCase):
    username = 'vahid@sh.com'
    email = ''
    def test_signup_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_url_byname(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
    
    def test_signup_page_form(self):
        response = self.client.post(reverse('signup'),{'username':'vahids','email':'vahid@vahid.com', 'password1':"Va@143124716", 'password2':'Va@143124716'})
        self.assertEqual(response.status_code, 302)

    def test_signup_form(self):
        get_user_model().objects.create_user(self.username, self.email )

        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)



    
