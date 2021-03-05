# # for Beautifulsoup version check 
# import bs4
# print(bs4.__version__)

from bs4 import BeautifulSoup 
import requests

res = requests.get("https://search.daum.net/nate?nil_suggest=btn&w=tot&DA=SBC&q=%ED%8C%8C%EC%9D%B4%EC%8D%AC")


if (res.status_code == 200):
    html = res.text
    soup = BeautifulSoup(html, "html.parser")
    netizen_lists_top = soup.find(id = 'netizen_lists_top')

    print('Option 1. get top-3 related keywords')
    wsns = netizen_lists_top.find_all(class_='wsn')
    iter = 0 
    while iter < 3 : 
        wsn = wsns[iter]
        a = wsn.find_all('a')
        text = a[0].get_text()
        
        print(text)
        iter += 1


    print('Option 2. get texts in target_keywords')
    
    target_keywords = ["파이썬 강좌", "파이썬 프로그래밍", "파이썬 자격증"]
    
    crawled_keywords = []
    for idx in range(len(wsns)) : 
        wsn = wsns[idx]
        a = wsn.find_all('a')
        text = a[0].get_text()

        if text in target_keywords : 
            crawled_keywords.append(text)

    print(crawled_keywords)

else : 
    print('Failed to read web page')
    print(res.status_code)