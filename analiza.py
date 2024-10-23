import requests
import csv
import re

r = requests.get('https://arxiv.org/list/math/2024-01')

#["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

for x in ["01"]:
    r = requests.get(f"https://arxiv.org/list/math/2024-" + x)
    besedilo = r.text[r.text.index("articles"):]

sekcije = besedilo.split('</dd>')



#with open("zbrani_podatki.csv", "w", newline='', encoding="utf-8") as izhod:
#    writer = csv.writer(izhod)
#    writer.writerow(["ID", "leto", "naslov", "avtor", "področje"])
#    ID = 0
#
#    for delo in sekcije:

#with open("filmi.csv", "w", newline = None, encoding="utf-8") as f:
#    writer = csv.DictWriter(f, fieldnames=["id", "naslov", "autor", "področje"])
#    writer.writeheader()
#    for članek in besedilo:
#        writer.writerow(članek)

avtor1 = r"(\+.\">)([^<]*)"
for i in (range(3)):
    avtor = r"(<div class='list-authors'>.*</div>)"
    lola = re.search(avtor, sekcije[i]).group(0).split('</a>,')
    for element in lola:
        print(re.search(avtor1, element).group(2))


#def izlusci_sifro_in_naslov(niz):
#    vzorec = r'<a href="/title/tt(?P<sifra>\d+)/\?ref_=adv_li_tt">(?P<naslov>.*?)</a>'
#    pojavitev = re.search(vzorec, niz)
#    sifra = int(pojavitev.group('sifra'))
#    naslov = pojavitev.group('naslov')
#    return sifra, naslov
#
#    <a href="/title/tt0076759/?ref_=adv_li_tt">Star Wars: Episode IV - A New Hope</a>')
