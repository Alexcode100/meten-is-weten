#BEGIN
print('----------------------------------------------')
print('Welkom bij de:\nCircusdirecteur voor Circus HotelDeBotel Vacature')
print('----------------------------------------------')
print('Laten we beginnen!')
#BEGIN



#NAAM EN LEEFTIJD
Naam = (input('Wat is uw voor en achternaam? '))
Leeftijd = (input('Wat is uw leeftijd? '))
#NAAM EN LEEFTIJD 



#PRAKTIJK ERVARING CODE
PraktijkErvaring = (input('Hoeveel jaar praktijk ervaring heeft u met Dieren-Dressuur? '))
if int(PraktijkErvaring) >=4:
    Diploma = (input('Bent u in bezit van een Diploma MBO-4 ondernemen? (ja/nee) '))
else:
    PraktijkErvaring2 = (input('Hoeveel jaar ervaring heeft u met jongleren? '))
    if int(PraktijkErvaring2) >=5:
        Diploma = (input('Bent u in bezit van een Diploma MBO-4 ondernemen? (ja/nee) '))
    else:
        PraktijkErvaring3 = (input('Hoevel jaar praktijk ervaring heeft u met acrobatiek? '))
        if int(PraktijkErvaring3) >=3:
            Diploma = (input('Bent u in bezit van een Diploma MBO-4 ondernemen? (ja/nee) '))
        else:
            print("------------------------------------------------------------------------------------")
            print("Sorry! Aangezien u niet genoeg Praktijk ervaring heeft kunt u niet bij ons komen werken.")
            print("------------------------------------------------------------------------------------")
#PRAKTIJK ERVARING CODE



#DIPLOMA CODE
if Diploma == "ja":
    Rijbewijs = (input('Bent u in bezit van een geldig Vrachtwagen rijbewijs(ja/nee) '))
else: 
    Rijbewijs = (input('Bent u in bezit van een geldig Vrachtwagen rijbewijs(ja/nee) '))
#DIPLOMA CODE



#RIJBEWIJS CODE
if Rijbewijs == "ja":
    HogeHoed = (input('Bent u in bezit van een hoge hoed?(ja/nee) '))
else: 
    HogeHoed = (input('Bent u in bezit van een hoge hoed?(ja/nee) '))  
#RIJBEWIJS CODE



#HOGEHOED CODE
if HogeHoed == "ja":
    ManVraag = (input('Bent u een (Man/Vrouw) '))
else:
    ManVraag = (input('Bent u een (Man/Vrouw) '))
#HOGEHOED CODE



#SNORVRAAG VOOR ALS MAN
if ManVraag == "Man":
    SnorVraag = (input('Heeft u een snor? (ja/nee) '))  
    if SnorVraag == "ja":
        BreedteSnorVraag = input('Hoe breed is uw snor? ')
        if int(BreedteSnorVraag) >=10:
            Lengte = input('Hoelang bent u? ')
        else:
            Lengte = input('Hoelang bent u? ')
    else:
        Lengte = input('Hoelang bent u? ')
#SNORVRAAG VOOR ALS MAN



#KRULLHAARVRAAG VOOR ALS VROUW
else:
    Krullhaar = input('Heeft u rood krullhaar? (ja/nee) ')
    if Krullhaar == "ja":
        LengteHaar = input('Hoelang is uw haar? ')
        if int(LengteHaar) >=20:
           Lengte = input('Hoelang bent u? ')
        else:
            Lengte = input('Hoelang bent u? ')
    else:
        Lengte = input('Hoelang bent u? ')
#KRULLHAARVRAAG VOOR ALS VROUW



#GEWICHT
if int(Lengte) >=150:
    Gewicht = input('Hoeveel weegt u? ')
else:
    Gewicht = input('Hoeveel weegt u? ')
#GEWICHT



#CERTIFICAAT + GESLAAGD JA OF NEE
if int(Gewicht) >=90:
    Certificaat = input('Heeft u de certificaat “Overleven met gevaarlijk personeel”? (ja/nee) ')
else:
    Certificaat = input('Heeft u de certificaat “Overleven met gevaarlijk personeel”? (ja/nee) ')

if Certificaat == "ja":
    print('---------------------------------------------\nGefeliciteerd!\nU bent aangenomen als ruimtevuilnisman!\n---------------------------------------------')
else:
    print('------------------------------\nHelaas!\nU moet de certificaat "Overleven met gevaarlijk personeel” hebben om bij ons te kunnen werken!\n---------------------------------------------')
#CERTIFICAAT + GESLAAGD JA OF NEE



















    