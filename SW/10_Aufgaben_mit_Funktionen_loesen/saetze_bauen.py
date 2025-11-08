# Das Programm soll Subjekt, Prädikat, Objekt aus Listen 
# zufällig auswählen und einen Satz bauen

# Bibliothek importieren
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

# Funktion aufrufen
for i in range(5):
    # Satz bauen
    mein_satz = bau_den_satz(subjekt, prädikat, objekt)
    # Ergebnis drucken
    print(mein_satz)
