# Programm erstellt das Wörterbuch Deutsch - Englisch
# aus dem vorhandenen Wörterbuch   English - Deutsch
# Funktioniert nur, wenn jeder Wert nur einmal im Dictionary vorkommt!
# Dann können Schlüssel und Werte mit einer Programmzeile vertauscht werden

# Wörterbuch Englisch - Deutsch importieren
from Woerterbuch import *

# Erstelle ein Wörterbuch mit v,k für alle k,v in einer Liste von Tupeln
deutsch_englisch = dict((v,k) for k,v in englisch_deutsch.items())

# neues Wörterbuch ausgeben
print(deutsch_englisch)

# Schlüssel und Werte ausgeben
print(deutsch_englisch.keys())
print(deutsch_englisch.values())
