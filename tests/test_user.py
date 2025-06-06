from python_expert.models.user import User, InvalidPasswordException

from unittest import TestCase

class TestUser(TestCase):

    def setUp(self):
        self.user1 = User('Peter', 'peter@tip.nl')

    def test_instantiation(self):
        self.assertIsInstance(self.user1, User)

    def test_username(self):
        self.assertEqual(self.user1.name, 'Peter')

    def test_email(self):
        self.assertEqual(self.user1.e_mail, 'peter@tip.nl')

    def test_correct_password(self):
        self.user1.set_password('Welkom01!')
        self.assertTrue(self.user1.check_password('Welkom01!'))

    def test_incorrect_password(self):
        self.user1.set_password('Welkom01!')
        self.assertFalse(self.user1.check_password('HACKER!'))

    def test_invalid_password(self):
        with self.assertRaises(InvalidPasswordException):
            self.user1.set_password('')
            self.user1.set_password('aaaa')
            self.user1.set_password('aaaaa')
    

