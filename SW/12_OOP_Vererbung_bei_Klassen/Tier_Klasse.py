# Vererbung in Python

# Eltern-Klasse
class Tier():
    """ Klasse für das Erstellen von Säugetieren """

    def __init__(self, rufname, farbe, alter):
        self.rufname = rufname
        self.farbe = farbe
        self.alter = alter
        self.schlafdauer = 0

    def tut_reden(self, anzahl = 1):
        print(self.rufname, "sagt: ", anzahl * "miau ")

    def tut_schlafen(self, dauer):
        print(self.rufname, "schläft jetzt", dauer , "Minuten ")
        self.schlafdauer += dauer
        print(self.rufname, "Schlafdauer insgesamt:", self.schlafdauer, "Minuten")

# Kind-Klasse für Katzen
class BauplanKatzenKlasse(Tier):
    """ Klasse für das Erstellen von Katzen """

    def __init__(self, rufname, farbe, alter):
        """ Initalisieren über Eltern-Klasse """
        super().__init__(rufname, farbe, alter)

# Kind-Klasse für Hunde
class Hund(Tier):
    """ Klasse für das Erstellen von Hunden """

    def __init__(self, rufname, farbe, alter):
        """ Initalisieren über Eltern-Klasse """
        super().__init__(rufname, farbe, alter)

    def tut_reden(self, anzahl = 1):
        """ Überschreiben der Methode der Eltern-Klasse """
        print(self.rufname, "sagt: ", anzahl * "WAU ")

# Instanz Sammy erstellen
katze_sammy = BauplanKatzenKlasse("Sammy", "orange", 3)
print(katze_sammy.farbe)

# Instanz Bello erstellen
hund_bello = Hund("Bello", "braun", 5)
print(hund_bello.farbe)

# Methoden aufrufen
hund_bello.tut_schlafen(4)
katze_sammy.tut_schlafen(5)
hund_bello.tut_schlafen(2)
katze_sammy.tut_reden(1)
hund_bello.tut_reden(3)
