from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, RequestFactory
from django.urls import reverse

from forumApp.posts.views import IndexView

UserModel = get_user_model()


class TestIndexViewIntegration(TestCase):

    def setUp(self):
        self.credentials = {
            "username": "anton",
            "email": "admin@admin.com",
            "password": "anton12qwert"
        }

    def test__get_template_names__authenticated_user__returns_auth_template(self):
        user = UserModel.objects.create_user(
                **self.credentials
        )

        self.client.login(**self.credentials)

        response = self.client.get(reverse('index'))

        self.assertEqual(response.template_name, ['common/index_logged_in.html'])

    def test__get_template_names__not_authenticated_user__returns_index_no_user_template(self):
        user = AnonymousUser()

        response = self.client.get(reverse('index'))

        self.assertEqual(response.template_name, ['common/index.html'])


class TestIndexViewUnit(TestCase):
    """
    Closer to inittest testing -> Faster,
    Doesn't test middlewares,
    Mocks the request,
    """
    def setUp(self):
        self.credentials = {
            "username": "anton",
            "email": "admin@admin.com",
            "password": "anton12qwert"
        }
        self.factory = RequestFactory()

    def test__get_template_names__authenticated_user__returns_auth_template(self):
        request = self.factory.get(reverse('index'))
        request.user = UserModel.objects.create_user(
                **self.credentials
        )

        response = IndexView.as_view()(request)

        self.assertEqual(response.template_name, ['common/index_logged_in.html'])

    def test__get_template_names__not_authenticated_user__returns_index_no_user_template(self):
        request = self.factory.get(reverse('index'))
        request.user = AnonymousUser()

        response = IndexView.as_view()(request)

        self.assertEqual(response.template_name, ['common/index.html'])