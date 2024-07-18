def get_mask_card_number(card_number: str) -> str:
    """
    принимает на вход номер карты и возвращает ее маску
    :param card:
    :return:
    """
    # 7000 79** **** 6361

    number = card_number[:6] + len(card_number[6:-4]) * "*" + card_number[-4:]
    # sep_card_number = [number[i:i + 4] for i in range(0, 16, 4)]

    lst = []
    for i in range(0, 16, 4):
        lst.append(number[i : i + 4])
    return " ".join(lst)


print(get_mask_card_number("7000792289606361"))


def get_mask_account(bank_aсcount: str) -> str:
    """
    Функция возвращает маску счета
    """
    return "*" * 2 + bank_aсcount[-4:]


print(get_mask_account("73654108430135874305"))


def card_number():
    return None
