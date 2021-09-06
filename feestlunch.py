
Croissantjes = int(input("Hoeveel croissantjes? : "))
PrijsCroissant = float(input("Hoe duur is een croissantje? : "))
Stokbroden = int(input("Hoeveel stokbroden? : "))
PrijsStokbrood = float(input("Hoe duur is een stokbrood? : "))
Korting = float(input("Hoeveel korting krijg je? : "))


bedrag = ((Croissantjes * PrijsCroissant) + (Stokbroden * PrijsStokbrood) - Korting)

factuurtekst = "De feestlunch kost je bij de bakker " + str(bedrag) + " euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!"

print(factuurtekst)