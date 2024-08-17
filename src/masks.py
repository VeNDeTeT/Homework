import logging
import os

# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла логов относительно текущей директории
rel_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rel_file_path)

# Добавляем логгер, который записывает логи в файл.
logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(abs_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

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
