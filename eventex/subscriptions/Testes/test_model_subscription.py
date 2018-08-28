from django.test import TestCase
from eventex.subscriptions.models import Subscription
from datetime import datetime


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Cesar Fois',
            cpf='12345678901',
            email='fois2010@gmail.com',
            phone='12-996450253'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_create(self):
        """Subscription must have an auto creata at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Cesar Fois', str(self.obj))
