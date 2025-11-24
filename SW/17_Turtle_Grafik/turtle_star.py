# Zeichne einen Stern
# Quelle: https://docs.python.org/3/library/turtle.html
# Geändert: Kommentare hinzugefügt

# Alle Namen von Bibliothek turtle importieren
from turtle import *

# Linienfarbe rot
color('red')
# Füllfarbe gelb
fillcolor('yellow')

# Langsamste Geschwindigkeit
#speed(1)

# Füllen beginnen
begin_fill()

# Loop
while True:
    # 200 Schritte vorwärts
    forward(200)
    # Linksdrehung um 170°
    left(170)
    # wenn Turtle wieder in Home-Postion
    if abs(pos()) < 1:
        # abbrechen
        break

# Füllen beenden
end_fill()

# Turtle event loop
mainloop()
