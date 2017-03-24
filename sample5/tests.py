import json
import unittest
import app


class AppTestCase(unittest.TestCase):
    def test_welcome(self):
        with app.app.test_client() as client:
            response = client.get('/welcome/John')
            data = json.loads(response.data)
            assert data['username'] == 'John'

    def test_welcome_and_show_id(self):
        with app.app.test_client() as client:
            response = client.get('/welcome/John/show_id/1')
            data = json.loads(response.data)
            assert data['username'] == 'John'
            assert data['user_id'] == 1

if __name__ == '__main__':
    unittest.main()

