import sys
import requests
from bs4 import BeautifulSoup

URL = 'https://github.com/DragutuMatei?page=1&tab=repositories'
try:
    response1 = requests.request('GET', url=URL)
except:
    # stiu ca nu e profesional acest print dar ayaye
    print("nu ai net fraere")
    sys.exit(1)
    

URL = 'https://github.com/DragutuMatei?page=2&tab=repositories'
try:
    response2 = requests.request('GET', url=URL)
except:
    # stiu ca nu e profesional acest print dar ayaye
    print("nu ai net fraere")
    sys.exit(1)

soup1 = BeautifulSoup(response1.content, 'html.parser')
soup2 = BeautifulSoup(response2.content, 'html.parser')

repositories1 = soup1.findAll("li", attrs={'class':'col-12 d-flex flex-justify-between width-full py-4 border-bottom color-border-muted public source'})
repositories2 = soup2.findAll("li", attrs={'class':'col-12 d-flex flex-justify-between width-full py-4 border-bottom color-border-muted public source'})

f = open('low_budget_db.txt', 'w')

def scrie_aicea(repositories):
    for repo in repositories:
        denumire_repo = repo.find("h3", attrs={'class':'wb-break-all'}).find('a').text
        vizibilitate = repo.find('span', attrs={'class':'Label Label--secondary v-align-middle ml-1 mb-1'}).text
        try:
            limbaj = repo.find('span', attrs={'itemprop':'programmingLanguage'}).text
        except AttributeError as error:
            limbaj = ''
            
        string_de_scris = 'Proiectul ' + vizibilitate.strip() + ' "' + denumire_repo.strip() + '"'

        if not limbaj :
            string_de_scris += ' nu are precizat limbajul de programare'
        else:
            string_de_scris += ' a fost scris in ' + limbaj.strip()

        f.write(
            string_de_scris
        )
        f.write('\n')
        f.write(
            'https://github.com/DragutuMatei/' + denumire_repo.strip() + '\n')
        
        f.write('\n')
        f.write('\n')

scrie_aicea(repositories1)
scrie_aicea(repositories2)

f.close()

