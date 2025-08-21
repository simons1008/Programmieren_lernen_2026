# Der Computer soll die vom Benutzer erdachte Zahl erraten
# Der Benutzer hilft: Benutzer-Zahl ist g(rößer), k(leiner), e(rraten)

# Die Zahl liegt zwischen der unteren und der oberen Grenze

# untere Grenze
untere = 1

# obere Grenze
obere = 100

# Benutzer zum Ausdenken einer Zahl auffordern
print("Denke dir eine Zahl zwischen ", untere, " und ", obere)

# Auf die Bestätigung warten
taste = input("Drücke ENTER, wenn du fertig bist ")

# Vorbelegung der Benutzereingabe
benutzereingabe = ""

# Solange raten, bis Benutzer e eingibt
while benutzereingabe != "e":
    # Zahl raten
    x = (untere + obere)//2

    # Zahl ausgeben
    print("Der Computer rät ", x)

    # Benutzereingabe anfordern
    benutzereingabe = input("Ist deine Zahl g(rößer), k(leiner), e(rraten)?  ")

    # Benutzereingabe bewerten
    if benutzereingabe == "k":
        # obere Grenze verkleinern
        obere = max(untere, x - 1)
    elif benutzereingabe == "g":
        # untere Grenze vergrößern
        untere = min(obere, x + 1)
