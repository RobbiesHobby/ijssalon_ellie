prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}
aanbieding = prijzen["aardbei"] * 0.8 # subvraag 3 (met wijziging cf. toelichting door Peter bij jhuiswerk 6)
reclame_tekst = f"Vandaag in de aanbieding: aardbei-ijs, 1 liter slechts €{aanbieding}" # subvraag 4
reclame_tekst2 = reclame_tekst[:60] # subvraag 5
reclame_tekst3 = reclame_tekst2.upper() # subvraag 6
reclame_tekst4 = reclame_tekst3.split() # subvraag 7
for el in reclame_tekst4:
    # print(el) # subvraag 8
    if len(el)>=5: # subvraag 10
        print(el)
    else:
        print(el.lower()) # subvraag 9
    
# print(prijzen) # 'antwoord' subvraag 2
# print(aanbieding) # antwoord subvraag 3 (met wijziging cf. toelichting door Peter)
# print(reclame_tekst) # antwoord subvraag 4
# print(reclame_tekst2) # antwoord subraag 5
# print(reclame_tekst3) # antwoord subraag 6
# print(reclame_tekst4) # antwoord subraag 7