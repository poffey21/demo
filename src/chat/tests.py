from django.conf import settings
from django.test import TestCase
from django.urls import reverse

from . import models


class MessageTestCase(TestCase):
    """Quick and simple unit tests for Message Model"""

    def test_creation_of_message(self):
        """ Let's make sure we can create a message """
        obj = models.Message.objects.create(
            username='DL12924',
            message='This is a new message'
        )
        self.assertEqual(obj.message, u'This is a new message')

    def test_ordering_of_messages(self):
        """ Let's see if the order is correct """
        for i in range(99):
            models.Message.objects.create(
                username='DL12924',
                message='This is a new message'
            )
        last_message = models.Message.objects.create(
            username='DL12924',
            message='This is the newest message'
        )
        self.assertEqual(100, models.Message.objects.count())
        self.assertEqual(last_message, models.Message.objects.all().last())

    def test_new_subscription_page(self):
        self.client.login(username=settings.TEST_LDAP_USER)
        response = self.client.post(
            reverse('chat:chat-session'),
            {'message': 'this is a new message'},
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='chat/message_form.html')
