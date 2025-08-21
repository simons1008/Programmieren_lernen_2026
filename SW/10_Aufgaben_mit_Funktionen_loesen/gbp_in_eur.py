# Das Programm soll GPB in EUR umrechnen und eine Tabelle ausgeben

# Input der Funktion ist eine Dezimalzahl in der Einheit GBP
# Output der Funktion ist eine Dezimalzahl in der Einheit EUR
# Umrechnungsfaktor 1 GBP = 1.21 EUR

# Funktion mit Datentyp
def gbp_in_eur(gbp: float) -> float:
    eur = gbp * 1.21
    return eur

# Input Liste anlegen
gbp_liste = []
for i in range(21):
    gbp_liste.append(i * 0.5)

# Output Liste (leer) anlegen
eur_liste = []

# Funktion aufrufen 
for x in gbp_liste:
    eur_liste.append(gbp_in_eur(x))

# Ergebnisse drucken
print("gbp    eur")
for x, y in zip(gbp_liste, eur_liste):
    print("{:5.2f} {:5.2f}".format(x, y))
