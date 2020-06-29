from django.urls import reverse,resolve
from django.test import TestCase
from boards.views import *
from boards.models import *
from django.contrib.auth.models import User


#
# class NewTopicsTest(TestCase):
#     def setUp(self):
#         Board.objects.create(name='Django',description='Django board.')
#         User.objects.create(username='Anu',email='anu@gmail.com',password='Anusha123')
#
#     def test_new_topics_view_success_status_code(self):
#         url=reverse('new_topics',kwargs={'board_id':1})
#         response=self.client.get(url)
#         self.assertEquals(response.status_code,200)
#
#     def test_new_topics_view_not_found_status_code(self):
#         url=reverse('new_topics',kwargs={'board_id':99})
#         response=self.client.get(url)
#         self.assertEquals(response.status_code,404)
#
#     def test_new_url_resolver_new_topic_view(self):
#         view=resolve('/boards/1/new/')
#         self.assertEquals(view.func,new_topics)
#
#     def test_new_topics_view_contains_link_back_to_homepage(self):
#         url=reverse('new_topics',kwargs={'board_id':1})
#         response=self.client.get(url)
#         home_page=reverse('home')
#         self.assertContains(response,'href="{0}"'.format(home_page))
#
#     def test_csrf(self):
#         url=reverse('new_topics',kwargs={'board_id':1})
#         response=self.client.get(url)
#         self.assertContains(response,'csrfmiddlewaretoken')
#
#     def test_new_topic_valid_post_data(self):
#         url=reverse('new_topics',kwargs={'board_id':1})
#         data={
#         'subject':'test title',
#         'message':'This is a test data'
#         }
#         response=self.client.post(url,data)
#         self.assertTrue(Topic.objects.exists())
#         self.assertTrue(Post.objects.exists())
#
#     def test_new_topic_invalid_post_data(self):
#         url = reverse('new_topics', kwargs={'board_id':1})
#         response = self.client.post(url, {})
#         self.assertEquals(response.status_code, 200)
#
#     def test_new_topic_invalid_post_data_empty_fields(self):
#         url = reverse('new_topics', kwargs={'board_id':1})
#         data = {
#             'subject': '',
#             'message': ''
#         }
#         response = self.client.post(url, data)
#         self.assertEquals(response.status_code, 200)
#         self.assertFalse(Topic.objects.exists())
#         self.assertFalse(Post.objects.exists())
#
#     def test_contains_form(self):
#         url = reverse('new_topics', kwargs={'board_id':1})
#         response = self.client.get(url)
#         form = response.context.get('form')
#         self.assertIsInstance(form, NewTopicsForm)
#
#     def test_new_topic_invalid_post_data(self):
#         url = reverse('new_topics', kwargs={'board_id':1})
#         response = self.client.post(url, {})
#         form = response.context.get('form')
#         self.assertEquals(response.status_code, 200)
#         self.assertTrue(form.errors)

class LoginRequiredTopicTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')
        self.url = reverse('new_topics',  kwargs={'board_id':1})
        self.response = self.client.get(self.url)

    def test_redirection(self):
        login_url = reverse('login')
        self.assertRedirects(self.response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))
