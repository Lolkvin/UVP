import requests
import csv
import re

#["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
ID = 1    
avtor = r"(<div class='list-authors'>.*</div>)"
avtor1 = r"(\+.\">)([^<]*)"
naslov = r'(Title:</span>)([^<]*)'



with open("zbrani_podatki.csv", "w", newline='', encoding="utf-8") as izhod:
    writer = csv.writer(izhod)
    writer.writerow(["ID", "naslov", "avtor", "mesec", "glavno področje", "ostala področja"])

    for skip in {"0", "2000", "4000"}:
        for a in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
            r = requests.get(f"https://arxiv.org/list/math/2024-" + a + "?skip=" + skip + "&show=2000")
            besedilo = r.text[r.text.index("articles"):]
            mesec = a
            sekcije = besedilo.split('</dd>')

            for i in range(len(sekcije) - 1):
                
                
                    #ID lahko damo svoj, najlazje je da gremo samo po vrsti
        
        
                    #izluščimo naslov posameznega dela
                    nas = re.search(naslov, sekcije[i]).group(2).strip()
        
        
                    #to ustvari seznam avtorjev posameznega dela
                    lola = re.search(avtor, sekcije[i]).group(0).split('</a>,')
                    seznam_avtorjev_dela = ""
                    for element in lola:
                            if re.search(avtor1, element) == None:
                                pass
                            else:
                                seznam_avtorjev_dela += f"{re.search(avtor1, element).group(2)}, "
        
                    #mesec je že prej določen, mogoče bom naredu 2 leti da lahk dodam še leto, idk
        
        
                    #glavno področje
                    gl_podrocje = re.search(r'(<span class="primary-subject">)([^<]*)(<)', sekcije[i]).group(2)
        
        
                    #stransko področje
                    if re.search(r'(<span class="primary-subject">)([^<]*)(</span>;)([^<]*)(</div>)', sekcije[i]) == None:
                        st_podrocje = "empty,"
                    else:
                        st_podrocje_list = re.search(r'(<span class="primary-subject">)([^<]*)(</span>;)([^<]*)(</div>)', sekcije[i]).group(4)[:-9].split(';')
                        st_podrocje = ""
                        for element in st_podrocje_list:
                            st_podrocje += element + ","
                            st_podrocje = st_podrocje.strip()
                    st_podrocje = st_podrocje[:-1]
        
        
        
                    writer.writerow([ID, nas, f'{seznam_avtorjev_dela[:-2]}', mesec, gl_podrocje, st_podrocje])
                    ID += 1

