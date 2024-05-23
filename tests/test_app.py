import pytest
from flask_testing import TestCase
from app_init import create_app

class MyTest(TestCase):

    def create_app(self):
        app = create_app()
        return app

    def test_home(self):
        response = self.client.get('/allOrders')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"message":"There are no orders."})