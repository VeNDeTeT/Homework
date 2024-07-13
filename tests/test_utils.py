import json
from unittest.mock import Mock

from src.utils import get_info


def test_get_info():
    mock_get_info = Mock(return_value=r"C:\Users\Admin\qwer\learn\sasha\Homework\Bank\date\operations.json")
    get_info = mock_get_info
    get_info(file_json=r"C:\Users\Admin\qwer\learn\sasha\Homework\Bank\date\operations.json") == r"C:\Users\Admin\qwer\learn\sasha\Homework\Bank\date\operations.json"
    mock_get_info.assert_called_once_with(file_json=r"C:\Users\Admin\qwer\learn\sasha\Homework\Bank\date\operations.json")