from typing import Iterable

# Вход функции
# [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]



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
    return sorted(filter_by_state, key=lambda date: date.get("date"), reverse=descending