import pytest

from src.masks import get_mask_account,get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7000123412345678", "7000 12** **** 5678"),
        ("1999432189600989", "1999 43** **** 0989"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_card_number_1(card_number_1):
    assert get_mask_card_number(card_number_1) == "7000 79** **** 6361"


def test_card_number_2(card_number_2):
    assert get_mask_card_number(card_number_2) == "7000 12** **** 5678"



def test_card_number_3(card_number_3):
    assert get_mask_card_number(card_number_3) == "1999 43** **** 0989"