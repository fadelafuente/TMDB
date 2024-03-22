from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase

from posts.models import Post
from django.contrib.auth import get_user_model
from django.utils import timezone, dateparse
from django.contrib.auth.models import AnonymousUser
import json

AppUser = get_user_model()

class TestPosts(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = AppUser.objects.create_user(email="testemail@domain.com", password="testpassword", username="testuser", first_name="test", last_name="user")

    # Not necessary to test, here for me to see how updating usernames would work
    def test_update_username(self):
        self.client.force_authenticate(user=self.user)

        data = {"username": "updatedUser"}
        response = self.client.patch("/auth/users/me/", data=json.dumps(data), content_type="application/json")
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], "updatedUser")