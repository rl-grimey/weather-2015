import requests, csv
from bs4 import BeautifulSoup

data = []

def scrapeStation(station):
    url = 'http://www.wunderground.com/history/airport/{}/{}/12/{}/DailyHistory.html'
    day = range(1,32)
    year = range(1948, 2015)

    for i in year:
        for j in day:
            formattedURL = url.format(station, i, j)
            page = requests.get(formattedURL)
            soup = BeautifulSoup(page.text, "html.parser")
            table = soup.find(id='historyTable').find_all('span', class_='wx-value')

            meanTemp = table[0].text
            maxTemp = table[2].text
            minTemp = table[5].text

            if j == 31:
                print ("year: "+str(j), meanTemp)
            data.append({"year":i, "day":j, "meanTemp":meanTemp, "maxTemp":maxTemp, "minTemp":minTemp})

scrapeStation("KIOW")

with open("december-scraped-IC.csv", "wb") as outfile:
    attrNames = ["day", "year", "meanTemp", "maxTemp", "minTemp"]
    writer = csv.DictWriter(outfile, fieldnames=attrNames)

    writer.writeheader()
    writer.writerows(data)
