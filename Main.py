# Zainstalujcie:
# pymysql
# requests
# bs4

import pymysql, requests, bs4

# 1. Wykonaj żądanie GET dla zadresu https://www.imdb.com/chart/top?ref_=nv_mv_250

class ImdbScrapper:

    def getTop250(self):
        try:
            html = requests.get("https://www.imdb.co/chart/top?ref_=nv_mv_250")
            print("Wykonano poprawnie żądanie")
        except:
            print("Ups! Coś poszło nie tak")

imdb = ImdbScrapper()
imdb.getTop250()