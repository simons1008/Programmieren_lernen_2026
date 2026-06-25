# Der Computer soll die vom Benutzer erdachte Zahl erraten
# Der Benutzer hilft: Benutzer-Zahl ist g(rößer), k(leiner), e(rraten)

# Die Zahl liegt zwischen der unteren und der oberen Grenze

# untere Grenze
untere = 1

# obere Grenze
obere = 100

# Anzahl der Versuche
versuche = 0

# Benutzer zum Ausdenken einer Zahl auffordern
print("Denke dir eine Zahl zwischen ", untere, " und ", obere)

# Auf die Bestätigung warten
input("Drücke ENTER, wenn du fertig bist ")

# Vorbelegung der Benutzereingabe


# Solange raten, bis Benutzer e eingibt


    # Zahl raten
    x = (untere + obere)//2

    # Versuche hochzählen
    versuche += 1

    # Zahl ausgeben
    print("Der Computer rät ", x)

    # Benutzereingabe anfordern
    benutzereingabe = input("Ist deine Zahl g(rößer), k(leiner), e(rraten)?  ")

    # Benutzereingabe bewerten


        # obere Grenze verkleinern


        # untere Grenze vergrößern


# Ende
print("Zahl erraten! Versuche =", versuche)
input("Fertig? ")

