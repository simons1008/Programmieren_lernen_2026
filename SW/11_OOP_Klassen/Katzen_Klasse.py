# Objektorientierte Programmierung

# Klassendefinition
class BauplanKatzenKlasse():
    """ Klasse für das Erstellen von Katzen
    Hilfetext ideal bei mehreren Programmierern in
    einem Projekt oder bei schlechtem Gedächtnis """

    # Methoden der Klasse
    def __init__(self, rufname, farbe, alter):
        self.rufname = rufname
        self.farbe   = farbe
        self.alter   = alter
        # Dauer aufaddieren
        self.schlafdauer = 0

    def tut_miauen(self, anzahl = 1):
        print(anzahl * "miau ")

    def tut_schlafen(self, dauer):
        print(self.rufname, "schläft jetzt", dauer , "Minuten ")
        self.schlafdauer += dauer
        print(self.rufname, "Schlafdauer insgesamt:", self.schlafdauer, "Minuten ")

# Instanz Sammy erstellen
katze_sammy = BauplanKatzenKlasse("Sammy", "orange", 3)
print(katze_sammy.rufname)
print(katze_sammy.farbe)
print(katze_sammy.alter)

# Instanz Soni erstellen
katze_soni = BauplanKatzenKlasse("Soni", "getigert", 2)

# Methoden von Katze Sammy aufrufen
katze_sammy.tut_miauen(3)
katze_sammy.tut_schlafen(3)
katze_sammy.tut_schlafen(6)
katze_sammy.tut_miauen(5)
katze_sammy.tut_schlafen(10)

# Methode von Katze Soni aufrufen
katze_soni.tut_schlafen(5)
