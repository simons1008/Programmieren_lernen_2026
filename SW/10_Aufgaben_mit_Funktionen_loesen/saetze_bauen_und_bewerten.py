# Das Programm soll Subjekt, Prädikat, Objekt aus Listen 
# zufällig auswählen und einen Satz bauen
# Das Programm soll zählen, wie oft der Satz richtig war
# Das Programm soll abbrechen, wenn jeder Satz mindesten 1 Mal richtig war
# Das Programm soll seine Laufzeit messen und ausgeben 

# Bibliotheken importieren
import time
import random

# Beispielsätze
subjekt = ["Der Hund", "Die Journalistin", "Der Maler"] 
prädikat = ["vergräbt", "interviewt", "malt"]	
objekt = ["den Knochen", "den Bürgermeister", "ein Bild"]

# Input der Funktion sind die Listen Subjekt, Prädikat und Objekt 
# Output der Funktion ist der Satz

# Funktion mit Datentyp
def bau_den_satz(subjekt: list[str], prädikat: list[str], \
                 objekt: list[str]) -> str:
    mein_subjekt = random.choice(subjekt)
    mein_prädikat = random.choice(prädikat)
    mein_objekt = random.choice(objekt)
    mein_satz = mein_subjekt + " " + mein_prädikat + " " + mein_objekt
    return mein_satz	

# Funktion nimmt einen Zeitstempel
def ticks_us():
    return int(time.perf_counter_ns()/1000.0)

# Funktion berechnet die Differenz zwischen zwei Zeitstempeln    
def ticks_diff(ticks1, ticks2):
    return ticks2 - ticks1

# Zeit nehmen
ticks1 = ticks_us()

# Zähler initialisieren
hund = 0
journalistin = 0
maler = 0

# Funktion aufrufen
for i in range(50):
    # Satz bauen
    mein_satz = bau_den_satz(subjekt, prädikat, objekt)

    # Ergebnis drucken
    print(mein_satz)

    # Ergebnis bewerten    
    if mein_satz == "Der Hund vergräbt den Knochen":
        print("Hund richtig!")
        hund += 1     
    elif mein_satz == "Die Journalistin interviewt den Bürgermeister":
        print("Journalistin richtig!")
        journalistin += 1
    elif mein_satz == "Der Maler malt ein Bild":
        print("Maler richtig!")
        maler += 1

    # aufhören, wenn jeder Satz mindestens 1 mal richtig war
    if (hund >= 1) and (journalistin >= 1) and (maler >= 1):
        break

# Zusammenfassung:
print("Anzahl der Durchläufe i =", i)
print("hund =", hund, "journalistin =", journalistin, "maler = ", maler)

# Zeit nehmen
ticks2 = ticks_us()

# Laufzeit anzeigen
print("Das Programm lief", ticks_diff(ticks1, ticks2), "Mikrosekunden")

# Abfrage
input("Fertig?")

