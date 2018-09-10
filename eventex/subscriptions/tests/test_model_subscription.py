from django.shortcuts import resolve_url as r

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

    def test_create_at(self):
        """Subscription must have an auto create at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Cesar Fois', str(self.obj))

    def test_paid_default_to_False(self):
        """By default paid must be False."""
        self.assertEqual(False, self.obj.paid)

    def test_get_absolute_url(self):
        url = r('subscriptions:detail',  self.obj.pk)
        self.assertEqual(url, self.obj.get_absolute_url())