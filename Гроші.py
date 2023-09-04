import urllib.request
import requests
from  bs4 import BeautifulSoup as bs

# opener = urllib.request.build_opener()
# response = opener.open("https://uk.wikipedia.org/wiki/Головна_сторінка")
# print(response.read())

r = requests.get("https://privatbank.ua/rates-archive")
html = bs(r.text, "html.parser")
data = html.find_all("div",class_= "sale")
for i in data:
    print(i.span.text)

converter = "CurrencyConverter"()

amount = float(input("Введіть кількість валюти вашої країни: "))
from_currency = input("Введіть код валюти вашої країни: ")
to_currency = 'USD'; "EUR" ; "PLN"

converted_amount = converter.convert(amount, from_currency, to_currency)

if converted_amount is None:
    print("Не вдалося отримати курс валют")
else:
    print(f"{amount} {from_currency} = {converted_amount} USD")

