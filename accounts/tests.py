from django.test import TestCase
from django.contrib.auth.models import User


class UserModelTest(TestCase):
    def user_admin(self):
        return User.objects.create(username="admin", first_name="first_name", last_name="last_name", password="123abc$", is_staff=True, is_superuser=True)

    def user_critic(self):
        return User.objects.create(username="critic", first_name="first_name", last_name="last_name", password="123abc$", is_staff=True, is_superuser=False)

    def test_create_admin_success(self):
        admin = self.user_admin()
        self.assertIsNotNone(admin.id)
        self.assertTrue(isinstance(admin, User))

    def test_create_critic_success(self):
        critic = self.user_critic()
        self.assertIsNotNone(critic.id)
        self.assertTrue(isinstance(critic, User))
