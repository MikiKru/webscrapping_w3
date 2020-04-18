# Zainstalujcie:
# pymysql
# requests
# bs4

import pymysql, requests

# 1. Wykonaj żądanie GET dla zadresu https://www.imdb.com/chart/top?ref_=nv_mv_250
from bs4 import BeautifulSoup


class ImdbScrapper:
    # self.obiekt -> zakres wydoczności obejmuje całąklasę ImdbScrapper
    def getTop250(self):
        try:
            self.page = requests.get("https://www.imdb.com/chart/top?ref_=nv_mv_250")
            print("Wykonano poprawnie żądanie")
            # print(self.page.content)
        except:
            print("Ups! Coś poszło nie tak")
    def scrappingTop250(self):
        # page.content -> zwraca zawartość żądania get
        html_content = BeautifulSoup(self.page.content, 'html.parser')
        # print(html_content.prettify())
        titles = html_content.find_all(class_ = "titleColumn")
        ratings = html_content.find_all(class_ = "ratingColumn imdbRating")
        # seq = ['a','b','c']
        # for i, o in enumerate(seq):
        #     print(i, o)
        for index, title in enumerate(titles):
            titles[index] = str(titles[index]).split(">")[2].replace("</a","")
            ratings[index] = str(ratings[index]).split(">")[2].replace("</strong","")
            print(titles[index])
            print(ratings[index])

imdb = ImdbScrapper()
imdb.getTop250()
imdb.scrappingTop250()