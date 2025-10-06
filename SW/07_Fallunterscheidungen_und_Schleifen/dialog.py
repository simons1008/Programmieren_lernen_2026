# Der Computer fragt, bis der Benutzer "e" eingibt
benutzereingabe = ""

# while-Schleife
while benutzereingabe != "e":
    benutzereingabe = input("Gib einen Buchstaben ein: ")
    print(benutzereingabe)
    if benutzereingabe == "k":
        print("kleiner")
    elif benutzereingabe == "g":
        print("größer")

# Die Mitte zwischen zwei Zahlen berechnen
untere = 50
obere = 100
mitte = (untere + obere) // 2
print("Die Mitte zwischen", untere, "und", obere, "ist:", mitte)
