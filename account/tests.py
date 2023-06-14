from os import stat
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.



class AccountTest(APITestCase):

    def test_register(self):
        _data = {
            "first_name"  : "Abhijeet",
            "last_name" : "Gupta",
             "username" : "abhijeet01",
            "password" : "123",
        }

        _response = self.client.post('/api/account/register/', data = _data, format="json")
        _data = _response.json()
        print
        self.assertEqual(_response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(_data['status'],True)
