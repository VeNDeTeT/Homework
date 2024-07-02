import pytest


from src.gener_data import  transactions

@pytest.mark.parametrize(
    "transactions, currency, expected",
    [(transactions, "USD", 939719570), (transactions, "USD", 939719570)],
)