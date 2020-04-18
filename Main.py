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
        years = html_content.find_all('span', attrs={'class' : 'secondaryInfo'})
        ratings = html_content.find_all(class_ = "ratingColumn imdbRating")
        refs = html_content.find_all(class_ = "titleColumn")

        for index, title in enumerate(titles):
            titles[index] = str(titles[index]).split(">")[2].replace("</a","")
            years[index] = str(years[index]).split("(")[1].split(")")[0]
            ratings[index] = str(ratings[index]).split(">")[2].replace("</strong","")
            refs[index] = "https://www.imdb.com" + str(refs[index]).split('href="')[1].split('"')[0]
            print(titles[index])
            print(years[index])
            print(ratings[index])
            print(refs[index])
            # self.getMovieDetails(refs[index])
    def getMovieDetails(self, url):
        details = requests.get(url)
        details_html = BeautifulSoup(details.content, 'html.parser')
        print(details_html.prettify())
        # pobierz reżysera
        # pobierz gwiazdy 3 pozycje
        kolumna = details_html.findAll(class_="credit_summary_item")
        rezyser = (str(kolumna).split(">")[4])[:-3]
        aktorzy = (str(kolumna).split("Stars:")[1].split(">")[2]).replace("</a", ""), \
                  (str(kolumna).split("Stars:")[1].split(">")[4]).replace("</a", ""), \
                  (str(kolumna).split("Stars:")[1].split(">")[6]).replace("</a", "")
        print(aktorzy)
        print(rezyser)


imdb = ImdbScrapper()
imdb.getTop250()
imdb.scrappingTop250()