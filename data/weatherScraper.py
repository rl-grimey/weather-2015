import requests, csv
from bs4 import BeautifulSoup

data = []

def scrapeStation(station):
    url = 'http://www.wunderground.com/history/airport/KIOW/{}/12/{}/DailyHistory.html'
    formattedURL = url.format(1948, 1)

    page = requests.get(formattedURL)
    soup = BeautifulSoup(page.text, "html.parser")
    table = soup.find(id='historyTable').find_all('span', class_='wx-value')

    meanTemp = table[0].text
    maxTemp = table[1].text
    minTemp = table[2].text


scrapeStation("test")
