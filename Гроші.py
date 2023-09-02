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

