from django.test import TestCase
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class TestUserModel(TestCase):
    def test__valid__str__method(self):
        user =  UserModel.objects.create_user(
            username='pesho',
            password='dgfherg3f3',
            email='pesho@pesho.com',
        )

        self.assertEqual(
            str(user),
            user.email,
        )