import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()  # Create a test client
        self.app.testing = True       # Enable testing mode

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Inventory App Running 15th may...")

if __name__ == '__main__':
    unittest.main()
