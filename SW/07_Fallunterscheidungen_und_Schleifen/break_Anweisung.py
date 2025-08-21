# Eine unendliche Schleife abbrechen

# Variable initialisieren
durchgang = 1

# Unendliche Schleife 
while True:
    # Variable ausgeben
    print("durchgang =", durchgang)
    # Variable inkrementieren
    durchgang = durchgang + 1
    # Bedingung für Abbruch 
    if durchgang > 10:
        break

# Diese Anweisung gehört nicht mehr zur Schleife
print("Nach der Schleife")
