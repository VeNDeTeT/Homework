import pytest
from src.masks import get_mask_card_number


@pytest.fixture
def card_number_1():
    return "7000792289606361"

@pytest.fixture
def card_number_2():
    return "7000123412345678"

@pytest.fixture
def card_number_3():
    return "199943218960010"

@pytest.fixture
def bank_aсcount_1()
    return "73654103330135224305"