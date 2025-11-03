# globale und lokale Variable in der Funktion

# Funktion liest eine globale Variable
def bspfunktion_global_lesen():
    print("---- Funktion liest eine globale Variable ----")
    # die gelesene Variable ist implizit global!
    print("Variablenwert in Funktion:", variablenWert)

# Funktion gibt der Variable einen Wert
def bspfunktion_lokal_schreiben():
    print("---- Funktion gibt der Variable einen Wert ----")
    # die Variable bekommt einen Wert, damit ist sie lokal!
    variablenWert = "IN der Funktion"
    print("Variablenwert in Funktion:", variablenWert)

# Funktion liest eine globale Variable und gibt ihr einen Wert
def bspfunktion_global_lesen_schreiben():
    # die Variable wird als global vereinbart
    global variablenWert
    print("---- Funktion liest eine globale Variable und gibt ihr einen Wert ----")
    # die gelesene globale Variable
    print("Variablenwert in Funktion 1:", variablenWert)
    # die globale Variable bekommt einen Wert
    variablenWert = "IN der Funktion"
    print("Variablenwert in Funktion 2:", variablenWert)

# die Variable außerhalb der Funktion ist global
variablenWert = "außerhalb der Funktion"

print("\nVariablenwert vor dem Aufruf der Funktion:", variablenWert)
# Aufruf der Funktion
bspfunktion_global_lesen()
print("Variablenwert nach dem Aufruf der Funktion:", variablenWert)

print("\nVariablenwert vor dem Aufruf der Funktion:", variablenWert)
# Aufruf der Funktion
bspfunktion_lokal_schreiben()
print("Variablenwert nach dem Aufruf der Funktion:", variablenWert)

print("\nVariablenwert vor dem Aufruf der Funktion:", variablenWert)
# Aufruf der Funktion
bspfunktion_global_lesen_schreiben()
print("Variablenwert nach dem Aufruf der Funktion:", variablenWert)
