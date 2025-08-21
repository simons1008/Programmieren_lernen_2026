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

    def fahren(self, km):
        print(self.besitzer, "fährt", km, "km")
        self.kmstand += km
        print("Insgesamt ist", self.besitzer, self.kmstand, "km gefahren")

    def klingeln(self, anzahl = 1):
        print(anzahl * "Bim ")

    def abstellen(self):
        print(self.besitzer, "hat sein Fahrrad abgestellt")

    def kilometerstand(self):
        print("Der Kilometerstand ist", self.kmstand, "km")    
        
# Instanz erstellen
mein_fahrrad = BauplanFahrradKlasse("Martin", "Silber", "Touring", 24)
print(mein_fahrrad.besitzer)
print(mein_fahrrad.farbe)
print(mein_fahrrad.typ)
print(mein_fahrrad.gaenge)

# Methoden aufrufen
mein_fahrrad.klingeln(3)
mein_fahrrad.fahren(15)
mein_fahrrad.fahren(5)
mein_fahrrad.klingeln(2)
mein_fahrrad.fahren(3)
mein_fahrrad.abstellen()
mein_fahrrad.kilometerstand()
