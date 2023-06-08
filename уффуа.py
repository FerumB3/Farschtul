# import urllib.request
#
# opener = urllib.request.build_opener()
# responser = opener.open("https://httpbin.org/get")
#
# print(responser.read())
#
# import  requests
# response = requests.get("https://httpbin.org/get")
#
# print(response.content)

# import urllib.request
#
# opener = urllib.request.build_opener()
# responser = opener.open("https://httpbin.org/get")
#
# print(responser.read())
#
# import  requests
# response = requests.get("https://httpbin.org/get")
#
# print(response.content)

# import  requests
# response = requests.get("https://httpbin.org/get")
#
# print(response.content)
# print(f'Datetype - {type(response.text)}')

# import requests
# response= requests.post('https://httpbin.org/get', data="Test data",headers={"h1":"Test title"})
#
# print(response.text)

# import requests
# response= requests.post('https://httpbin.org/get', data={"Test form":"me_fornm"})

# import requests
# res_parse_list=[]
#
# respones = requests.get("https://coinmarketcap.com")
# respones_text = respones.text
# respones_parse = respones_text.split("<span>")
# for parse_elem_1 in respones_parse:
#     if parse_elem_1.startswith("$"):
#         for parse_elem_2 in parse_elem_1.split("</span>"):
#             if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
#                 res_parse_list.append(parse_elem_2)
#
# bitcoin_exchage_rate = res_parse_list[0]
#
# print(bitcoin_exchage_rate)

from  bs4 import BeautifulSoup
import requests

respons=requests.get("https://coinmarketcap.com")

if respons.status_code==200
    soup=BeautifulSoup(respons.text, featurs="html.parsel")
    soup_list = soup.find_all("a",{'href':'/currencies/bitcoin/markets/'}})
    # for elem in soup_list:
    #     print(elem)
    res = soup_list[0].find("span")



