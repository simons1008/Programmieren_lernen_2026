# Programm erzeugt ein Fenster und setzt die Wände eines Irrgartens hinein
# - Eine Funktion setzt die Wände in das Fenster
# Modul für die Turtle-Grafik importieren
import turtle
# Irrgarten-Klasse 
class Maze:
    """Klasse für den Bau eines Irrgartens"""
    # Methoden der Klasse
    def __init__(self):
        self.rows_in_maze = 11
        self.columns_in_maze = 22
        # turtle Objekt erzeugen und Aussehen festlegen 
        self.t = turtle.Turtle()
        self.t.shape("turtle")
        # Breite, Höhe und Koordinaten des Fensters festlegen
        self.wn = turtle.Screen()
        self.wn.setup(800, 400)
        self.wn.setworldcoordinates(0, 0, self.columns_in_maze, self.rows_in_maze)
    # Zeichne ein ausgefülltes Rechteck
    def draw_box(self, x, y, color):
        self.t.up() # Stift hoch
        self.t.goto(x, y)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down() # Stift runter
        self.t.begin_fill()
        # Rechteck zeichnen und füllen
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
    # Setze Wände in das Fenster
    def draw_maze(self):
        # Farben: 'white','black','red','green','blue','cyan','yellow','magenta'
        self.draw_box(0, 0, "orange")
        self.draw_box(self.columns_in_maze - 1, self.rows_in_maze - 1, "magenta")
        self.draw_box(self.columns_in_maze//2, self.rows_in_maze//2, "cyan") 
        # Farbe der Schildkröte
        self.t.color("black")
        self.t.fillcolor("blue")
        self.wn.update()
# Instanz erzeugen
my_maze = Maze()
# Irrgarten zeichnen
my_maze.draw_maze()
my_maze.t.up() # Stift hoch
# Schildkröte in Home-Position
my_maze.t.home()
# Turtle event loop
my_maze.wn.mainloop()
