import unittest
import json
from app import create_app

class TestPlaceCreation(unittest.TestCase):

    def setUp(self):

        self.app = create_app()
        self.client =self.app.test_client()
        self.app.testing = True

    sef test_create_place(self):

        place_data = {
            "title": "Opulent Haven",
            "description": "Where comphort meets sophistication",
            "price": 540.0,
            "latitude": 27.48333,
            "longitude": -29.31667,
            "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        }

        response = self.client.post(
            '/api/v1/places/',
            data=json.dumps(place_data),
            content_type='application/json'
        )


        self.assertEquel(response.status_code, 201)


        response_data = json.loads(response.data)
        self.assertEqual(response_data['title'], place_data['title'])
        self.assertEqual(response_data['description'], place_data['description'])
        self.assertEqual(response_data['price'], place_data['price'])
        self.assertEqual(response_data['latitude'], place_data['latitude'])
        self.assertEqual(response_data['logitude'], place_data['longitude'])
        self.assertEqual(response_data['owner_id'], place_data['owner_id'])

    def tearDown(self):

        pass

if __name__== '__main__':
    unittest.main()
