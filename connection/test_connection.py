import unittest
from unittest.mock import patch
from connection.connect import Response


class TestResponse(unittest.TestCase):

    def test_response(self):
        with patch('connection.connect.requests.get') as mock_get:
            mock_get.return_value.status_code = 404

            obj = Response()
            response = obj.get()
            main_page = obj.main_page

        self.assertEqual(response.status_code, 404)
        self.assertEqual(main_page, "You will see 404 custom page")


if __name__ == "__main__":
    unittest.main()
