# from django.urls import reverse,resolve
# from django.test import TestCase
# from django.contrib.auth.models import User
# from accounts.views import *
# from django.contrib.auth.forms import UserCreationForm
# from accounts.forms import SignupForm
#
#
# class SignUpTests(TestCase):
#     def setUp(self):
#         url = reverse('signup')
#         self.response = self.client.get(url)
#
#     def test_signup_status_code(self):
#         url = reverse('signup')
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)
#
#     def test_signup_url_resolves_signup_view(self):
#         view = resolve('/accounts/signup/')
#         self.assertEquals(view.func, signupview)
#
#     def test_csrf(self):
#         self.assertContains(self.response, 'csrfmiddlewaretoken')
#
#     def test_contains_form(self):
#         form = self.response.context.get('form')
#         self.assertIsInstance(form, SignupForm)
#
# class SuccessfulSignUpTests(TestCase):
#     def setUp(self):
#         url = reverse('signup')
#         data = {
#             'username': 'Anusha',
#             'password1': 'Anusha123',
#             'password2': 'Anusha123'
#         }
#         self.response = self.client.post(url, data)
#         self.home_url = reverse('home')
#
#     # def test_redirection(self):
#     #     self.assertRedirects(self.response, self.home_url)
#     #
#     # def test_user_creation(self):
#     #     self.assertTrue(User.objects.exists())
#     #
#     # def test_user_authentication(self):
#     #     response = self.client.get(self.home_url)
#     #     user = response.context.get('user')
#     #     self.assertTrue(user.is_authenticated)
#
#     def test_signup_status_code(self):
#         self.assertEquals(self.response.status_code, 200)
#
#     def test_form_errors(self):
#         form = self.response.context.get('form')
#         self.assertTrue(form.errors)
#
#     def test_form_inputs(self):
#         self.assertContains(self.response, '<input', 5)
#         self.assertContains(self.response, 'type="text"', 1)
#         self.assertContains(self.response, 'type="email"', 1)
#         self.assertContains(self.response, 'type="password"', 2)
#
#     def test_dont_create_user(self):
#         self.assertFalse(User.objects.exists())
