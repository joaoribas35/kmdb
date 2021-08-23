from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status


# class MovieViewTest(TestCase):
#     def test_status_admin_create_movie_success(self):
#         client = APIClient()

#         client.login(username='admin', password='1234abc$')
#         token = Token.objects.get(user__username='admin')
#         client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

#         body = {
#             "title": "O Poderoso Chefão 2",
#             "duration": "175m",
#             "genres": [
#                 {"name": "Crime"},
#                 {"name": "Drama"}
#             ],
#             "premiere": "1972-09-10",
#             "classification": 14,
#             "synopsis": "Don Vito Corleone (Marlon Brando) é o chefe de uma 'família' ..."
#         }

#         response = client.post('/api/movies/', body, format="json")
#         self.assertEquals(response.status_code, 201)

#     def test_response_admin_create_movie_success(self):
#         client = APIClient()

#         client.login(username='admin', password='1234abc$')
#         token = Token.objects.get(user__username='admin')
#         client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

#         body = {
#             "title": "O Poderoso Chefão 2",
#             "duration": "175m",
#             "genres": [
#                 {"name": "Crime"},
#                 {"name": "Drama"}
#             ],
#             "premiere": "1972-09-10",
#             "classification": 14,
#             "synopsis": "Don Vito Corleone (Marlon Brando) é o chefe de uma 'família' ..."
#         }

#         response = client.post('/api/movies/', body, format="json")

#         result = response.json()

#         self.assertIsNotNone(result["id"])
#         self.assertIsNotNone(result["title"])
#         self.assertIsNotNone(result["duration"])
#         self.assertIsNotNone(result["genres"])
#         self.assertIsNotNone(result["premiere"])
#         self.assertIsNotNone(result["classification"])
#         self.assertIsNotNone(result["synopsis"])
