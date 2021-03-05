# # for Beautifulsoup version check 
# import bs4
# print(bs4.__version__)

from bs4 import BeautifulSoup 
import requests

res = requests.get("http://example.com/")


if (res.status_code == 200):
    html = res.text
    soup = BeautifulSoup(html, "html.parser")
    print(soup.find('h1').get_text())
else : 
    print('Failed to read web page')
    print(res.status_code)