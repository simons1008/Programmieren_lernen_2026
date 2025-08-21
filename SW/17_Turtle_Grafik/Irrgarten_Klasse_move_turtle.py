# Programm erzeugt ein Fenster und setzt die Wände eines Irrgartens hinein
# - Die Wände werden aus einer Datei eingelesen
# - Die Wände sind in einer Liste von Listen abgelegt
# - Eine Funktion setzt die Wände in das Fenster
# - Eine Funktion bewegt die Schildkröte
# Modul für die Turtle-Grafik importieren
import turtle
# Zeichen für Wand und Freiraum
START = "S"
OBSTACLE = "+"
BLANK = " "
# Irrgarten-Klasse 
class Maze:
    """Klasse für den Bau eines Irrgartens"""
    # Methoden der Klasse
    def __init__(self, maze_filename):
        # maze_list aus Datei lesen
        self.maze_list = []
        with open(maze_filename, "r") as maze_file:
            self.lines = maze_file.readlines()
            for line in self.lines:
                self.maze_list.append([ch for ch in line.rstrip("\n")])
        self.rows_in_maze = len(self.maze_list)
        self.columns_in_maze = len(self.maze_list[0])
        print("rows_in_maze =", self.rows_in_maze, "columns_in_maze =", self.columns_in_maze)
        # Start in maze_list suchen
        for row in range(self.rows_in_maze):
            for col in range(self.columns_in_maze):
                if self.maze_list[row][col] == START:
                    self.start_row = row
                    self.start_col = col
                    break
        print("start_row =", self.start_row, "start_col =", self.start_col)
        # turtle Objekt erzeugen und Aussehen festlegen 
        self.t = turtle.Turtle()
        self.t.shape("turtle")
        # Breite, Höhe und Koordinaten des Fensters festlegen
        self.wn = turtle.Screen()
        self.wn.setup(800, 400)
        self.wn.setworldcoordinates(0, 0, self.columns_in_maze, self.rows_in_maze)
    # Lies die Zeilennummer von unten
    def from_bottom(self, row):
        # Zeilen der Liste laufen von oben nach unten
        # y Koordinaten des Fensters laufen von unten nach oben 
        return (self.rows_in_maze - 1) - row
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
        # Animation der Schildkröte ausschalten
        self.wn.tracer(0)
        for row in range(self.rows_in_maze):
            for col in range(self.columns_in_maze):
                if self.maze_list[row][col] == OBSTACLE:
                    self.draw_box(col, self.from_bottom(row), "orange")
        # Farbe der Schildkröte
        self.t.color("black")
        self.t.fillcolor("blue")
        self.wn.update()
        # Animation der Schildkröte einschalten
        self.wn.tracer(1)
    # Bewege die Schildkröte
    def move_turtle(self, x, y):
        x += 0.5
        y += 0.5
        self.t.setheading(self.t.towards(x, y))
        self.t.goto(x, y)
    # Aktualisiere die Position der Schildkröte
    def update_position(self, row, col, val=None):
        # Wenn val angegeben: Element der Liste überschreiben
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, self.from_bottom(row))
# Roboter sucht den Weg, Schildkröte läuft mit
def search_from(maze, start_row, start_col):
    # Schildkröte auf die Startposition setzen
    maze.update_position(start_row, start_col, BLANK)
    # Der Roboter sucht den Weg ... folgt
# Instanz erzeugen
my_maze = Maze("maze3.txt")
# Irrgarten zeichnen
my_maze.draw_maze()
my_maze.t.up() # Stift hoch
# Schildkröte in Home-Position
my_maze.t.home()
# Suche den Weg vom Start zum Ausgang
search_from(my_maze, my_maze.start_row, my_maze.start_col) 
# Turtle event loop
my_maze.wn.mainloop()
