import requests
from bs4 import BeautifulSoup
import csv

with open('ppda.csv', 'w', newline='') as csvfile:
    for i in range(9577,9807):
        ppda_url = 'https://understat.com/match/' + str(i)
        ppda_data = requests.get(ppda_url)
        ppda_html = ppda_data.content
        soup = BeautifulSoup(ppda_html, 'lxml')
        ppda = soup.find("div", string='PPDA')
        home = ppda.findNext('div', {'class':"progress-value"})
        hometeam = soup.find("div", {'class':'roster-home'}).findNext('h3').text
        awayteam = soup.find("div", {'class':'roster-away'}).findNext('h3').text
        print (home.text, hometeam, home.findNext('div', {'class':"progress-value"}).text, awayteam)
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([home.text, hometeam, home.findNext('div', {'class':"progress-value"}).text, awayteam])
