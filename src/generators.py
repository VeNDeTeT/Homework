from typing import Dict, Generator


def filter_by_currency(transactions: list[Dict], currency: str = "USD") -> Generator[Dict[str,object], None, None]:
    """Возвращает итератор, который выдает по очереди операции в указанной валюте"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


