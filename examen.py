from tabulate import tabulate
import csv

#####################
####DATA INLEZEN!####
#####################
with open("dataset_diersoorten.csv", "r", encoding="utf-8") as d:
    lijst = []
    reader = csv.reader(d)

    for row in reader:
        lijst.append(row)

headers = lijst[0]
dieren_list = lijst[1:]

# =====================
# Functionaliteiten
# =====================

#toon alle data(tabulate)
def toon_dieren_data():
    print("##############Dieren lijst#############")
    print(tabulate(dieren_list, headers=headers, showindex=True))

#Toon alle unieke diersoorten
def unieke_diersoorten():
    dieren = set()
    for rij in dieren_list:
        dieren.add(rij[1])
    print(dieren)

#Toon alle unieke landen
def unieke_landen():
    landen = set()
    for rij in dieren_list:
        landen.add(rij[4])
    print(landen)

#Toon alle dieren van diersoort x(bvb zoogdier) (alles in tabulate)
def toon_dierensoort_x():
    # welke soorten
    unieke_diersoorten() #oproepen van mijn unieke dierensoorten
    soort = input("Welke soort wil je zien?").capitalize()
    soort_data = [x for x in dieren_list if soort == x[1]]
    print(tabulate(soort_data, headers=headers))

#Voeg dier toe
def voeg_dier_toe():
    naam = input("Naam?").capitalize()
    soort = input("Soort?").capitalize()
    latijnsenaam = input("Latijnsenaam?").capitalize()
    geslacht = input("Geslacht").upper()
    landvanoorkomst = input("Landvanoorkomst?").capitalize()
    lengte = int(input("Lengte in cm?"))
    gewicht = float(input("Gewicht in kg?"))                        #float want .00
    nieuw_dier = [naam,soort,latijnsenaam,geslacht,landvanoorkomst,lengte,gewicht]
    dieren_list.append(nieuw_dier)
    toon_dieren_data()

#Verwijder een dier
def verwijder_dier():
    toon_dieren_data()
    index = int(input("Geef het nummer van het dier dat je wilt verwijderen:"))
    if index < len(dieren_list):
        dieren_list.pop(index)
    else:
        print("Dier kan niet verwijderd worden")

#Pas het gewicht aan van dier x
def pas_gewicht_aan():
    #wie? nieuwe_gewicht
    toon_dieren_data()
    index = int(input("Geef het nummer van het dier:"))
    if index < len(dieren_list):
        nieuw_gewicht = float(input("Geef het nieuwe gewicht in kg:"))
        dieren_list[index][6] = nieuw_gewicht #index rij(welke dier) 6de plaats staat gewicht
    else:
        print("kan gewicht niet aanpassen")

#Toon alle dieren zwaarde dan x kilo.
def toon_zwaarder_dan_x():
    res = []
    gewicht = float(input("geef het minimum gewicht van het dier in kg:"))
    for kg in dieren_list:
        if gewicht <= float(kg[6]):
            res.append(kg)
    print(tabulate(res,headers=headers))

#Sorteer op naam_dier(a-z)
def sorteer_op_naam_dier():
    res = sorted(dieren_list,key=lambda x:x[0])
    print(tabulate(res,headers=headers))

#Update data
def update_data():
    with open("dataset_diersoorten.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(dieren_list)

    print("Data opgeslagen in dataset_diersoorten.csv")

# =====================
# MENU VIA DICTIONARY
# =====================

functies = {
    "1": toon_dieren_data,
    "2": unieke_diersoorten,
    "3": unieke_landen,
    "4": toon_dierensoort_x,
    "5": voeg_dier_toe,
    "6": verwijder_dier,
    "7": pas_gewicht_aan,
    "8": toon_zwaarder_dan_x,
    "9": sorteer_op_naam_dier,
    "10": update_data
}

# =====================
# interface
# =====================

while True:

    print("\n")
    print("=" * 20)
    print("   Dierensoorten   ")
    print("=" * 20)
    print("1  - Toon alle dieren data")
    print("2  - Toon alle unieke dierensoorten")
    print("3  - Toon alle unieke landen")
    print("4  - Toon iedereen van dierensoort x")
    print("5  - Voeg een dier toe")
    print("6  - Verwijder een dier")
    print("7  - Pas het gewicht aan van dier x")
    print("8  - Toon alle dieren die meer dan x kilo wegen")
    print("9  - Sorteer op naam_dier")
    print("10 - Update data naar csv")
    print("0  - Stoppen")

    keuze = input("\nMaak een keuze: ")

    if keuze == "0":
        print("Programma afgesloten.")
        break

    if keuze in functies:
        functies[keuze]()
    else:
        print("Ongeldige keuze.")