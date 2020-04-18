import requests
from bs4 import BeautifulSoup

def getTwitterPagination():
    twitter_page = requests.get("https://twitter.com/search?q=%22Do%20Polski%22&src=trend_click")
    twitter_html = BeautifulSoup(twitter_page.content, 'html.parser')
    users = twitter_html.find_all(class_ = 'css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0')
    tweets = twitter_html.find_all(class_ = 'css-1dbjc4n')
    print(users)
    print(tweets)

getTwitterPagination()