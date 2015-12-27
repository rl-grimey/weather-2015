import requests, csv
from bs4 import BeautifulSoup

data = []

def scrapeStation(station):
    url = 'http://www.wunderground.com/history/airport/{}/2015/{}/{}/DailyHistory.html'
    day = range(1,32)
    month = range(1,12)

    for i in month:
        for j in day:
            formattedURL = url.format(station, i, j)
            page = requests.get(formattedURL)
            soup = BeautifulSoup(page.text, "html.parser")
            table = soup.find(id='historyTable').find_all('span', class_='wx-value')

            meanTemp = table[0].text
            maxTemp = table[2].text
            minTemp = table[5].text
            #averageMeanTemp
            averageMaxTemp = table[3].text
            averageMinTemp = table[6].text
            recordMaxTemp = table[4].text
            recordMinTemp = table[7].text
            #Add in years for record max/min

            print("Month: "+str(i) + ", Day: " + str(j))

            data.append({
                "month":i,
                "day":j,
                "meanTemp":meanTemp,
                "maxTemp":maxTemp,
                "minTemp":minTemp,
                "averageMaxTemp":averageMaxTemp,
                "averageMinTemp":averageMinTemp,
                "recordMaxTemp":recordMaxTemp,
                "recordMinTemp":recordMinTemp
            })

scrapeStation("KIOW")

with open("2015-scraped-IC.csv", "wb") as outfile:
    attrNames = data[0].keys()
    writer = csv.DictWriter(outfile, fieldnames=attrNames)

    writer.writeheader()
    writer.writerows(data)
