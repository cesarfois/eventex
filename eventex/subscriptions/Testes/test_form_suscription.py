from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubcriptionFormTest(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()

    def test_form_has_fields(self):
        """Form must have 4 Fields."""
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(self.form.fields))