import json
import unittest
import app


class AppTestCase(unittest.TestCase):
    def test_login(self):
        request_data = {
            'username': 'admin',
            'password': '123'
        }
        with app.app.test_client() as client:
            response = client.post(
                '/login',
                data=json.dumps(request_data),
                content_type='application/json'
            )
            print(response)
            data = json.loads(response.data)
            assert response.status_code == 200
            assert data['message'] == 'Welcome Admin'

    def test_login_fail(self):
        request_data = {
            'username': 'admin',
            'password': '1234'
        }
        with app.app.test_client() as client:
            response = client.post(
                '/login',
                data=json.dumps(request_data),
                content_type='application/json'
            )
            data = json.loads(response.data)
            assert response.status_code == 401
            assert data['message'] == 'Auth fail'

if __name__ == '__main__':
    unittest.main()

