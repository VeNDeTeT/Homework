import json
from typing import Any


def get_info(file_json: str) -> Any:
    """
    Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.
    """

    with open(file_json, encoding="utf-8") as f:
        try:
            trans = json.load(f)
            return trans
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []



