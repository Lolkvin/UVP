import requests
import csv
import re

r = requests.get('https://arxiv.org/list/math/2024-01')

#["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

for a in ["01"]:
    r = requests.get(f"https://arxiv.org/list/math/2024-" + a)
    besedilo = r.text[r.text.index("articles"):]
    mesec = a

sekcije = besedilo.split('</dd>')
avtor = r"(<div class='list-authors'>.*</div>)"
avtor1 = r"(\+.\">)([^<]*)"
naslov = r'(Title:</span>)([^<]*)'



with open("zbrani_podatki.csv", "w", newline='', encoding="utf-8") as izhod:
    writer = csv.writer(izhod)
    writer.writerow(["ID", "naslov", "avtor", "mesec", "področje"])
    ID = 1

    for i in range(len(sekcije) - 1):


        #ID lahko damo svoj, najlazje je da gremo samo po vrsti


        #izluščimo naslov posameznega dela
        nas = re.search(naslov, sekcije[i]).group(2).strip()


        #to ustvari seznam avtorjev posameznega dela
        lola = re.search(avtor, sekcije[i]).group(0).split('</a>,')
        seznam_avtorjev_dela = ""
        for element in lola:
                seznam_avtorjev_dela += f"{re.search(avtor1, element).group(2)}, "

        #mesec je že prej določen, mogoče bom naredu 2 leti da lahk dodam še leto, idk


        #področje
        if re.search(r'(<span class="primary-subject">)([^<]*)(</span>;)([^<]*)(</div>)', sekcije[i]) == None:
            jara = re.search(r'(<span class="primary-subject">)([^<]*)(<)', sekcije[i]).group(2)
        else: jara = [re.search(r'(<span class="primary-subject">)([^<]*)(</span>;)([^<]*)(</div>)', sekcije[i]).group(2)] + re.search(r'(<span class="primary-subject">)([^<]*)(</span>;)([^<]*)(</div>)', sekcije[i]).group(4).split(';')[:-2]






        writer.writerow([ID, nas, f'{seznam_avtorjev_dela[:-2]}', '01', jara])
        ID += 1


