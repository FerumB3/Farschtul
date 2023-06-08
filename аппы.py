import requests
from bs4 import BeautifulSoup


class CurrencyConverter:
    def __init__(self):
        self.base_url = 'https://bank.gov.ua/'

    def get_exchange_rate(self, currency_code):
        url = f'{self.base_url}NBUStatService/v1/statdirectory/exchange?valcode={currency_code}&json'
        response = requests.get(url)
        data = response.json()
        exchange_rate = data[0]['rate'] if data else None
        return exchange_rate

    def convert(self, amount, from_currency, to_currency):
        from_rate = self.get_exchange_rate(from_currency)
        to_rate = self.get_exchange_rate(to_currency)

        if from_rate is None or to_rate is None:
            return None

        converted_amount = amount * (to_rate / from_rate)
        return converted_amount


# Приклад використання
converter = CurrencyConverter()

amount = float(input("Введіть кількість валюти вашої країни: "))
from_currency = input("Введіть код валюти вашої країни: ")
to_currency = 'USD'

converted_amount = converter.convert(amount, from_currency, to_currency)

if converted_amount is None:
    print("Не вдалося отримати курс валют")
else:
    print(f"{amount} {from_currency} = {converted_amount} USD")