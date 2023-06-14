
from urllib import response
from django.test import TestCase
from .models import *
from faker import Faker
fake = Faker()
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
# Create your tests here.

class FirstTestCase(APITestCase):

    fixtures = ['main.json']
    
   

    def setUp(self):
        print('setup called')

    # def test_equal(self):
    #     self.assertEqual(1 , 1)
    
    
    def test_blog_category(self):
        return
        categories = ['Abc' , 'Def']

        for category in categories:
            obj = BlogCategory.objects.create(
               category_name = category
            )

            self.assertEquals(category , obj.category_name)

        objs = BlogCategory.objects.all()

        self.assertEqual(objs.count() ,3)

    
    def test_get_blog(self):
        _response = self.client.get('/api/home/?search=Tech', format="json")
        _data = _response.json()
        for data in _data['data']:
            category = data['category']
            self.assertEqual('Food', category['category_name'])


        self.assertEqual(_response.status_code, status.HTTP_200_OK)
        





