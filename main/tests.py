from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class MainPageTests(TestCase):
    def test_homepage_status_code(self):
        """Test that the homepage loads successfully."""
        response = self.client.get(reverse('home'))  # Replace 'home' with your homepage URL name
        self.assertEqual(response.status_code, 200)

    def test_homepage_content(self):
        """Test that the homepage contains the expected content."""
        response = self.client.get(reverse('home'))
        self.assertContains(response, "Welcome")  # Replace "Welcome" with text from your homepage

class AuthenticationTests(TestCase):
    def setUp(self):
        """Set up a test user."""
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_login_page_status_code(self):
        """Test that the login page loads successfully."""
        response = self.client.get(reverse('account_login'))
        self.assertEqual(response.status_code, 200)

    def test_successful_login(self):
        """Test that a user can log in successfully."""
        login = self.client.login(username='testuser', password='password')
        self.assertTrue(login)

    def test_logout_redirect(self):
        """Test that logging out redirects to the correct page."""
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('account_logout'))
        self.assertEqual(response.status_code, 302)  # Redirect status code
