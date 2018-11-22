from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class CoreTests(APITestCase):

    url_default = '/'

    def test_get_page_status_code(self):
        response = self.client.get(self.url_default)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
