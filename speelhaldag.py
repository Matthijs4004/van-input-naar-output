ToegangsPrijs = float(input("Hoe duur is een toegangsticket? : "))
PrijsPer5min = float(input("Hoe duur is 5 minuten met de VR? : "))


bedrag = ((ToegangsPrijs * 4) + (PrijsPer5min * 9 ))

factuurtekst = "Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar " + str(bedrag) + " euro "

print(factuurtekst)