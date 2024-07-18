import os
import requests
from dotenv import load_dotenv

load_dotenv('.env')


def return_amount_trans(transactions: dict) -> float:
    """
    Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях
    """
    amount = transactions["operationAmount"]["amount"]
    currency = transactions["operationAmount"]['currency']['code']
    if currency == 'RUB':
        return float(amount)
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        API_KEY = os.getenv('API_KEY')
        headers = {
            "apikey": f'{API_KEY}'
        }

        response = requests.get(url, headers=headers)
        # status_code = response.status_code
        # print(f"Статус код: {status_code}")
        data = response.json()
        return float(data['result'])


if __name__ == '__main__':
    r = (return_amount_trans(
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            }
        },))
    print(r)