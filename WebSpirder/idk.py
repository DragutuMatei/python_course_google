import requests
from bs4 import BeautifulSoup

URL = 'https://lpf.ro/liga-1'
r = requests.request('GET', url=URL)
print(r.content)

soup = BeautifulSoup(r.content, 'html.parser')
table = soup.find('table', attrs={'class':'clasament_general white-shadow'})

teams = []

for row in table.findAll('tr', attrs={'class':'echipa_row'}):
    echipa = row.find('td', attrs={'class':'echipa'}).text
    poz = row.find('td', attrs={'class':'poz'}).text
    pct = row.find('td', attrs={'class':'puncte'}).text
    teams.append({
        'echipa':echipa,
        'pozitia':poz,
        'puncte':pct
    })


print(teams)