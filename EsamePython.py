import csv

import requests
from bs4 import BeautifulSoup


def truncate():
    f = open('dati.csv', 'w')
    f.truncate()
    f.close()


lista = []


def scriviCSV(lista):
    # with open(r'D:\CodiceGit\Python\dati.csv', 'a') as outcsv:
    with open(r'/media/fabbro/Dati/CodiceGit/Python/dati.csv', 'a') as outcsv:
        # configure writer to write standard csv file
        writer = csv.writer(outcsv, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writerow(['Persona', 'Codice'])
        for x in lista:
            splittato = x.split(';')
            # Write item to outcsv
            writer.writerow([splittato[1], splittato[0]])


for numero in range(1, 111):
    r = requests.get("http://www.comuni-italiani.it/" + str(numero).rjust(3, '0') + "/sindaci.html")
    soup = BeautifulSoup(r.text, "html.parser")
    res = soup.findAll("font", text="Comune")
    comune = None
    for x in res:
        comune = x
    rigaintestazione = comune.parent.parent.parent
    nextriga = rigaintestazione
    while True:
        # rigaintestazione = comune.parent.parent.parent
        nextriga = nextriga.nextSibling.nextSibling
        if nextriga is None:
            break
        link_comune = nextriga.contents[0].contents[0].contents[0]
        stringa = str(numero).rjust(3, '0') + link_comune.attrs["href"][0:3] + ";" + nextriga.contents[1].text
        # print(stringa)
        lista.append(stringa)
# scrivi = open(r'C:\Users\Kerah\Desktop\sindaci.txt', 'w')
scrivi = open(r'/home/fabbro/Desktop/sindaci.txt', 'w')
for s in lista:
    scrivi.write(s + "\n")
truncate()
scriviCSV(lista)
scrivi.close()
