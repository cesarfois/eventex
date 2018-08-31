from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubcriptionFormTest(TestCase):
    def test_form_has_fields(self):
        """Form must have 4 Fields."""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must only accept digits"""
        form = self.make_validated_form(cpf='ABCD12345678901')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digiits."""
        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'lengh')

    def test_name_must_be_capitalized(self):
        """Nem must be capitalized"""
        #Henrique
        form = self.make_validated_form(name='CESAR fois')
        self.assertEqual('Cesar Fois', form.cleaned_data['name'])

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Cesar fois', cpf='12345678901',
                     email='fois2010@gmail.com', phone='12-996450253')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form