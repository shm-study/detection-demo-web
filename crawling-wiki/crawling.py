from bs4 import BeautifulSoup 
import requests

res = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

if (res.status_code == 200):
    html = res.text
    soup = BeautifulSoup(html, "html.parser")
    print(soup.select('.toctext'))
else : 
    print('Failed to read web page')
    print(res.status_code)