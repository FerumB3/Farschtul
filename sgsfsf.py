from  bs4 import BeautifulSoup
import requests

respons=requests.get("https://coinmarketcap.com")

if respons.status_code==200:
    soup=BeautifulSoup(respons.text, featurs="html.parsel")
    soup_list = soup.find_all("a",{'href':'/currencies/bitcoin/markets/'})
    # for elem in soup_list:
    #     print(elem)
    res = soup_list[0].find("span")