# Programm vergleicht die Kosten von zwei Stromtarifen 

# 1. Angebot: Input der Funktion ist eine Dezimalzahl in der Einheit kWh
#             Output der Funktion ist eine Dezimalzahl in der Einheit EUR

# Funktion mit Datentyp 
def watt_fuer_wenig(verbrauch: float) -> float:
    kosten = 15.6 + verbrauch * 0.32
    return kosten

# 2. Angebot: Input der Funktion ist eine Dezimalzahl in der Einheit kWh
#             Output der Funktion ist eine Dezimalzahl in der Einheit EUR

# Funktion mit Datentyp
def billig_strom(verbrauch: float) -> float:
    kosten = 12.8 + verbrauch * 0.36
    return kosten

# Input Liste anlegen
verbrauch_liste = range(0, 160, 10)
# 1. Angebot: Output Liste (leer) anlegen
kosten_liste1 = []
# 2. Angebot: Output Liste (leer) anlegen
kosten_liste2 = []

# Funktionen aufrufen
for x in verbrauch_liste:
    kosten_liste1.append(watt_fuer_wenig(x))
    kosten_liste2.append(billig_strom(x))

# Ergebnisse drucken
print(" Verbrauch  Watt für wenig  Billig Strom")
for x, y, z in zip(verbrauch_liste, kosten_liste1, kosten_liste2):
    print("{:10.2f} {:15.2f} {:13.2f}".format(x, y, z))

# Modul für das Plotten von Graphen importieren
import matplotlib.pyplot as plt

# Ergebnisse plotten
plt.plot(verbrauch_liste, kosten_liste1)
plt.plot(verbrauch_liste, kosten_liste2)
plt.xlabel("Verbrauch")
plt.ylabel("monatliche Kosten")
plt.show()
