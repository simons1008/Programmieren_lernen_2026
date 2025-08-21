# Kopiere und ändere den Inhalt einer Liste
# ACHTUNG: Eine Liste ist am Ort veränderbar (mutable object).
#          Schreib-Operationen in der Funktion ändern die Liste draußen!

# Funktion mit Datentyp
def addiere_zu_liste(meine_liste: list[int], zahl: int):
    for i in range(len(meine_liste)):
        meine_liste[i] += zahl

# Funktion mit Datentyp
def multipliziere_mit_liste (meine_liste: list[int], zahl: int):
    for i in range (len(meine_liste)):
        meine_liste[i] *= zahl

# Liste 
unsere_liste = [23, 456, 876]
print("Zu Beginn: ", unsere_liste)

# Addiere zur Liste
kopierte_liste = unsere_liste.copy()
addiere_zu_liste(kopierte_liste, 2)
print("Nach der Addition: ", kopierte_liste)

# Multipliziere  mit Liste
kopierte_liste = unsere_liste.copy()
multipliziere_mit_liste(kopierte_liste, 4)
print("Nach der Multiplikation: ", kopierte_liste)
