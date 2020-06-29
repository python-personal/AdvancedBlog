



from django.urls import reverse,resolve
from django.test import TestCase
from boards.views import *
from boards.models import *
from django.contrib.auth.models import User


# class BroadTopicsTest(TestCase):
#     def setUp(self):
#         Board.objects.create(name='Django',description='Django board.')
#
#     def test_board_topics_view_success_status_code(self):
#         url=reverse('board_topics',kwargs={'board_id':1})
#         response=self.client.get(url)
#         self.assertEquals(response.status_code,200)
#
#     def test_board_topics_view_not_found_status_code(self):
#         url=reverse('board_topics',kwargs={'board_id':99})
#         response=self.client.get(url)
#         self.assertEquals(response.status_code,404)
#
#     def test_board_url_resolver_boards_topic_view(self):
#         view=resolve('/boards/1/')
#         self.assertEquals(view.func,board_topics)
#
#     def test_board_topics_view_contains_link_back_to_homepage(self):
#         url=reverse('board_topics',kwargs={'board_id':1})
#         response=self.client.get(url)
#         home_page=reverse('home')
#         self.assertContains(response,'href="{0}"'.format(home_page))
#
#     def test_board_topics_view_contains_navigation_link(self):
#         board_topics_url=reverse('board_topics',kwargs={'board_id':1})
#         home_url=reverse('home')
#         new_topics_url=reverse('new_topics',kwargs={'board_id':1})
#         response=self.client.get(board_topics_url)
#         self.assertContains(response,'href="{0}"'.format(home_url))
#         self.assertContains(response,'href="{0}"'.format(new_topics_url))



# pagination:


def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func.view_class, TopicListView)
