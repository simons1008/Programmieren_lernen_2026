# Funktionen können Input und Output haben

# Funktionen können Input und Output haben
# Funktion ohne Input
def ausgabe():
    print("hier bin ich")
# Aufruf der Funktion
ausgabe()

# Funktion mit 2 Inputs
def ausgabe2a(wert1: int, wert2: int):
    print("wert1 =", wert1, "wert2 =", wert2)
# Aufruf der Funktion
ausgabe2a(5, 6)

# Funktion mit 2 Inputs und Vorgabe
def ausgabe2b(wert1: int, wert2: int = 15):
    print("wert1 =", wert1, "wert2 =", wert2)
# Aufruf der Funktion
ausgabe2b(5)

# Funktion mit 1 Input
def verdoppeln(wert: int) -> int:
    return wert * 2
# Aufruf der Funktion
ergebnis = verdoppeln(5)
print("ergebnis =", ergebnis)

# Funktion mit 2 Outputs
def wo_bin_ich() -> tuple[int, int]:
    x = 2 
    y = 4
    return x, y
# Aufruf der Funktion
x, y = wo_bin_ich()
print("x =", x, "y =", y)

# Funktion mit einer Liste als Input
def verteuerung(liste: list[float], p:[float]):
    for i in range(len(liste)):
        liste[i] *= 1 + p

# Liste anlegen
original = [9, 12, 12.5, 24.5]

# Liste kopieren
kopie = original.copy()

# Prozentsatz festlegen
p = 0.05

# Aufruf der Funktion
verteuerung(kopie, p)

# Original und Verteuerung
print("original =", original)
print("kopie =", kopie)
