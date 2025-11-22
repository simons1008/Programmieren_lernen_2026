# Zeichne ein Quadrat

# Modul für die Turtle-Grafik importieren
import turtle

# turtle Objekt erzeugen und Aussehen festlegen
t = turtle.Turtle()
t.shape("turtle")

# Bildschirmobjekt erzeugen
wn = turtle.Screen()

# Breite und Höhe des Fensters festlegen
wn.setup(800, 400)

# Koordinatensystem: links unten - rechts oben
wn.setworldcoordinates(0, 0, 22, 11)

# Farbe setzen
t.color('orange')

# Position setzen
t.goto(11, 5)

# Gefüllte Form starten
t.begin_fill()
# Quadrat zeichnen und füllen
for i in range(4):
    # Vorwärts 11 Schritte
    t.forward(5)
    # Rechtsherum drehen um 90 Grad
    t.right(90)
# Gefüllte Form beenden
t.end_fill()

# Farbe der Schildkröte
t.color("black")
t.fillcolor("blue")
wn.update()

# Schildkröte in Home-Position
t.home()

# Hauptschleife, damit die Turtle-Grafik angezeigt wird
wn.mainloop()
