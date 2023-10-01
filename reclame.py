# Bij vraag 12
from algemene_functies import mijn_functie_2

# Bij vraag 5
def aanbieding_1(smaak, prijs, korting):
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {(1-korting)*prijs} euro."
print(aanbieding_1("aardbei", 4, 0.1))

# Bij vraag 5, verbeterde versie (Zie feedback)
import math
def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs_voor_komma = math.floor((1 - korting) * prijs)
    nieuwe_prijs_na_komma = int(round(100 * ((1-korting)*prijs - math.floor((1-korting) * prijs)), 0))
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs_voor_komma},{nieuwe_prijs_na_komma} euro."
print(aanbieding_1("aardbei", 4, 0.1))

# Bij vraag 6
def inkomsten_totaal(inkomsten):
    totaal = 0
    for i in inkomsten:
        totaal += i
    return totaal
print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345]))

# Bij vraag 7
def inkomsten_totaal(inkomsten,btw):
    totaal = 0
    for i in inkomsten:
        totaal += i
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {totaal * btw} euro btw betaald dient te worden."
print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345],0.09))

# Bij vraag 8
def laag_en_hoog(mijn_lijst):
    return [max(mijn_lijst),min(mijn_lijst)]
print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))

# Bij vraag 9
def gemiddelde(mijn_lijst):
    totaal = 0
    for i in mijn_lijst:
        totaal += i
    return totaal / len(mijn_lijst)
print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))

# Bij vraag 10
def gemiddelde(mijn_lijst):
    totaal = 0
    for i in mijn_lijst:
        totaal += i
    return f"De gemiddelde inkomsten deze week zijn {int(totaal / len(mijn_lijst))} euro."
print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))

# Bij vraag 11
def meervoudig(invoer_lijst):
    return[laag_en_hoog(invoer_lijst)[0],laag_en_hoog(invoer_lijst)[1]]
print(meervoudig([10,5,3,2,1,2,9]))

# Bij vraag 12
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer
print(combinatie([10,5,3,2,1,2,9]))