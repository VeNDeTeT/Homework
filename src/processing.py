from typing import Iterable


def filter_by_state(list_of_data: Iterable[list[dict[str, str | int]]], condiyion: str="EXECUTED") -> Iterable[list[dict[str, str | int]]]:
    """Фильтрует транзакции по состоянию EXECUTED """
    filtered_list_EXECUTED = []
    for data in list_of_data:
        if data.get("state") == condiyion:
            filtered_list_EXECUTED.append(data)
    return filtered_list_EXECUTED


# 2

def filter_by_date(filter_by_state: list, descending: bool = True) -> list:
    """Фильтрует транзакции по дате"""
    return sorted(filter_by_state, key=lambda date: date.get("date"), reverse=descending)