# from unittest.mock import patch
# from nose.tools import assert_is_not_none
#
# from connection.connection_class import start_connection
#
#
# @patch('connection.connection_class.requests.get')
# def test_connection(mock_get):
#     # Configure the mock to return a response with an OK status code.
#     mock_get.return_value.ok = True
#
#     # Call the service, which will send a request to the server.
#     response = start_connection()
#
#     # If the request is sent successfully, then I expect a response to be returned.
#     assert_is_not_none(response)
#


# from nose.tools import assert_is_not_none
# #
# # # Local imports...
# # from connection.connection_class import start_connection
# #
# #
# # def test_request_response():
# #     # Call the service, which will send a request to the server.
# #     response = start_connection()
# #
# #     # If the request is sent successfully, then I expect a response to be returned.
# #     assert_is_not_none(response)


# Standard library imports...
from unittest.mock import Mock, patch

# Third-party imports...
from nose.tools import assert_is_not_none
from nose.tools import assert_is_none
# Local imports...
from connection.connection_class import start_connection


@patch('connection.connection_class.urllib.request.urlopen')
def test_connection(mock_urlopen):
    # Configure the mock to return a response with an OK status code.
    mock_urlopen.return_value = 404
    # a = Mock()
    # a.read.side_effect = ['404', '403']
    # mock_urlopen.return_value = a

    # Call the service, which will send a request to the server.
    response = start_connection()

    # If the request is sent successfully, then I expect a response to be returned.
    # assert_is_not_none(response)

    assert response == "You will see 404 custom page"

