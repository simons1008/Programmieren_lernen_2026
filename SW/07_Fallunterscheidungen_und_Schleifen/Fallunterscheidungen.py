# Fallunterscheidungen

# Der Benutzer soll eine Zahl eingeben:  
wert = input("Bitte Zahl eingeben ")

# String in Dezimalzahl umwandeln
wert = float(wert)

# Den eingegebenen Wert prüfen 
# Wenn eine Bedingung wahr ist:
# - werden die Befehle darunter ausgeführt
# - werden keine anderen Teile des if-Befehls ausgeführt
# Wenn keine Bedingung wahr ist:
# - werden die Befehle unter else ausgeführt. 
if wert == 4:
    print("Der Wert ist exakt 4")
    print("Ich gehöre auch noch zu der Bedingung")
elif wert == 5:
    print("Der Wert ist exakt 5")
elif wert == 6:
    print("Der Wert ist exakt 6")
else:
    print("Der Wert ist weder 4, noch 5, noch 6")
print("und hier geht es nach der Abfrage weiter")    
