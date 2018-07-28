from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Cesar Fois', cpf='12345678901',
                    email='fois2010@gmail.com', phone='12-996450253')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]


    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'fois2010@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Cesar Fois',
            '12345678901',
            'fois2010@gmail.com',
            '12-996450253',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

