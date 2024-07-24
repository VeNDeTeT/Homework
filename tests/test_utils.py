from unittest.mock import Mock


def test_get_info():
    mock_get_info = Mock(return_value=r"..\\date\\operations.json")
    get_info = mock_get_info
    get_info(file_json=r"..\\date\\operations.json") == r"..\\date\\operations.json"
    mock_get_info.assert_called_once_with(file_json=r"..\\date\\operations.json")
