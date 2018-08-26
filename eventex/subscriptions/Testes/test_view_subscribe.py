from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SuscribeGet(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        """Get /inscriçao/ must return status code 200 """
        self.assertEqual(200, self.resp.status_code)
    def test_template(self):
        """Must use template subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')
    def test_html(self):
        """Html must contain input tags"""
        tags = (('<form', 1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1))

        for text, count in tags:
            with  self.subTest():
                self.assertContains(self.resp, text, count)


    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """context must have subscrition form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Cesar Fois', cpf='12345678901',
                    email='fois2010@gmail.com', phone='12-996450253')
        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        """Valid POST Should redirect to /incricao/"""
        self.assertEqual(302, self.resp.status_code)

    def test_send_suscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())


class SubscribePostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/inscricao/',{})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.resp.status_code)

    def test_test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())

class SubscribeSucessMessage(TestCase):
    def test_message(self):
        data = dict(name='Cesar Fois', cpf='123456789901',
                    email='fois2010@gmail.com', phone='12-996450253')

        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso!')



