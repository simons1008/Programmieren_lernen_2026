# Objektorientierte Programmierung

# Klassendefinition
class BauplanFahrradKlasse():
    """ Klasse für das Erstellen von Fahrrädern
    Hilfetext ideal bei mehreren Programmierern in
    einem Projekt oder bei schlechtem Gedächtnis """

    # Methoden der Klasse
    def __init__(self, besitzer, farbe, typ, gaenge):
        self.besitzer = besitzer
        self.farbe  = farbe
        self.typ    = typ
        self.gaenge = gaenge
        # Kilometer aufaddieren
        self.kmstand = 0

    def klingeln(self, anzahl = 1):
        print(anzahl * "Bim ")

    def fahren(self, km):
        print(self.besitzer, "fährt", km, "km")
        self.kmstand += km
        print("Insgesamt ist", self.besitzer, self.kmstand, "km gefahren")

# Instanz mein_fahrrad erstellen
mein_fahrrad = BauplanFahrradKlasse("Martin", "silber", "Touring", 24)
print(mein_fahrrad.besitzer)
print(mein_fahrrad.farbe)
print(mein_fahrrad.typ)
print(mein_fahrrad.gaenge)

# Instanz leih_fahrrad erstellen
leih_fahrrad = BauplanFahrradKlasse("Peter", "rot", "Renn", 21)

# Methoden von mein_fahrrad aufrufen
mein_fahrrad.klingeln(3)
mein_fahrrad.fahren(15)
mein_fahrrad.fahren(5)
mein_fahrrad.klingeln(2)
mein_fahrrad.fahren(3)

# Methode von leih_fahrrad aufrufen
leih_fahrrad.fahren(45)
