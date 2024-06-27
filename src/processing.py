def filter_by_state(transactions: list, state: str = "EXECUTED") -> list:
    """Фильтрует транзакции по состоянию"""
    return [elem for elem in transactions if elem["state"] == state]


# 2

def filter_by_date(filter_by_state: list, descending: bool = True) -> list:
    """Фильтрует транзакции по дате"""
    return sorted(filter_by_state, key=lambda date: date.get("date"), reverse=descending)