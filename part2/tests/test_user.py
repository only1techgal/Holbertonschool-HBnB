import unittest
import json
from app import create_app

class TestUserCreation(unittest.TestCase):

    def setUp(self):

        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = TestUserCreation


    def test_create_user(self):

        user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com"
        }


        response = sef.client.post(
            '/api/v1/users/',
            data=json.dumps(user_data),
            content_type='application/json'
        )


        self.assertEqual(response.status_code, 201)


        response_data = json.loads(response.data)
        self.assertEqual(response_data['first_name'], user_data['first_name'])
        self.assertEqual(response_data['last_name'], user_data['last_name'])
        self.assertEqual(response_data['email'], user_data['email'])
    
    def tearDown(self):

        pass

if __name__== '__name__':
    unittest.main()

