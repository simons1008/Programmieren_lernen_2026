# Vererbung in Python

# Eltern-Klasse
class Zweirad():
    """ Klasse für das Erstellen von Zweirädern """

    # Methoden der Klasse
    def __init__(self, besitzer, farbe, typ, gaenge):
        self.besitzer = besitzer
        self.farbe  = farbe
        self.typ    = typ
        self.gaenge = gaenge
        # Kilometer aufaddieren
        self.kmstand = 0

    def klingeln(self, anzahl = 1):
        print(self.besitzer, "klingelt", anzahl * "Bim ")

    def fahren(self, km):
        print(self.besitzer, "fährt", km, "km")
        self.kmstand += km
        print("Insgesamt ist", self.besitzer, self.kmstand, "km gefahren")

# Kind-Klasse für Fahrräder
class BauplanFahrradKlasse(Zweirad):
    """ Klasse für das Erstellen von Fahrrädern """

    def __init__(self, besitzer, farbe, typ, gaenge):
        """ Initalisieren über Eltern-Klasse """
        super().__init__(besitzer, farbe, typ, gaenge)

# Kind-Klasse für Pedelecs
class Pedelec(Zweirad):
    """ Klasse für das Erstellen von Pedelecs
    mit der zusätzlichen Eigenschaft Kapazität """

    def __init__(self, besitzer, farbe, typ, gaenge, kapazitaet):
        """ Initalisieren über Eltern-Klasse """
        super().__init__(besitzer, farbe, typ, gaenge)
        # Kapazität in Wattstunden
        self.kapazitaet = kapazitaet

    def aufladen(self):
        print("Der Akku ist ausreichend geladen")

# Instanz meinFahrrad erstellen
mein_fahrrad = BauplanFahrradKlasse("Martin", "Silber", "Touring", 24)
print(mein_fahrrad.besitzer)

# Instanz deinPedelec erstellen
dein_pedelec = Pedelec("Hans", "Schwarz", "Touring", 12, 300)
print(dein_pedelec.besitzer)
print(dein_pedelec.kapazitaet)

# Methoden aufrufen
dein_pedelec.fahren(15)
mein_fahrrad.fahren(16)
dein_pedelec.fahren(3)
mein_fahrrad.klingeln(2)
dein_pedelec.klingeln(3)
dein_pedelec.aufladen()
