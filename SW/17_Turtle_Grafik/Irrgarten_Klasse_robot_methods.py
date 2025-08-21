# Programm erzeugt ein Fenster mit einem Irrgarten und bewegt Roboter und Schildkröte
# - Die Wände werden aus einer Datei eingelesen
# - Die Wände sind in einer Liste von Listen abgelegt
# - Eine Funktion setzt die Wände in das Fenster
# - Eine Funktion bewegt die Schildkröte
# - Mehrere Funktion lassen den Roboter schauen, gehen und drehen
# Modul für die Turtle-Grafik importieren
import turtle
# Zeichen für Wand und Freiraum
START = "S"
OBSTACLE = "+"
BLANK = " "
EXIT = "E"
# Richtungs-Eigenschaften
right_of  = {"up": "right", "down": "left" , "left": "up"  , "right": "down"}
left_of   = {"up": "left" , "down": "right", "left": "down", "right": "up"  }
delta_row = {"up": -1     , "down": 1      , "left": 0     , "right": 0     }
delta_col = {"up": 0      , "down": 0      , "left": -1    , "right": 1     }
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
        self.wn.setup(800, 400, 700)
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
    # Exit erreicht?
    def is_exit(self, row, col):
        return (
            row == 0
            or row == self.rows_in_maze - 1
            or col == 0
            or col == self.columns_in_maze - 1
        )
    # Geschwindigkeit und Richtung der Schildkröte, Richtung des Roboters festlegen
    def init_search(self):
        self.t.speed(3)
        self.t.setheading(90)
        heading = "up"
        return heading
    # schau nach vorne
    def look_forward(self, start_row, start_col, heading):
        # im Exit nicht nach vorne schauen!
        if self.is_exit(start_row, start_col) == True:
            return EXIT
        else:
            return self.maze_list[start_row + delta_row[heading]]\
                             [start_col + delta_col[heading]]
    # schau nach rechts
    def look_right(self, start_row, start_col, heading):
        return self.maze_list[start_row + delta_row[right_of[heading]]]\
                             [start_col + delta_col[right_of[heading]]]
    # mache einen Schritt
    def one_step(self, start_row, start_col, heading):
        start_row += delta_row[heading]
        start_col += delta_col[heading]
        return start_row, start_col
    # drehe dich nach rechts
    def turn_right(self, heading):
        self.t.right(90)
        return right_of[heading]
    # drehe dich nach links
    def turn_left(self, heading):
        self.t.left(90)
        return left_of[heading]
# Roboter sucht den Weg, Schildkröte läuft mit
def search_from(maze, start_row, start_col):
    # Schildkröte auf die Startposition setzen
    maze.update_position(start_row, start_col, BLANK)
    # Spur einschalten
    maze.t.down()
    # Richtung festlegen
    heading = maze.init_search()
    print(heading)
    # cmd initialisieren
    cmd = ""
    # Solange wiederholen, bis Benutzer "e" eingibt
    while cmd != "e":
        # cmd leeren
        cmd = ""
        # Solange wiederholen, bis Benutzer etwas eingibt
        while cmd == "":
            cmd = input("Kommando v[orne], h[and], l[inks], r[rechts], s[chritt, e[nde] ")
        print("Kommando =", cmd)
        if maze.is_exit(start_row, start_col) == True:
            print("Turtle im Exit!")
            print("Ende - du kannst das Turtle-Fenster jetzt schließen")
            break            
        elif cmd == "v":
            ch = maze.look_forward(start_row, start_col, heading)
            print(ch)
        elif cmd == "h":
            ch = maze.look_right(start_row, start_col, heading)
            print(ch)
        elif cmd == "l":
            heading = maze.turn_left(heading)
            print(heading)
        elif cmd == "r":
            heading = maze.turn_right(heading)
            print(heading)
        elif cmd == "s":
            start_row, start_col = maze.one_step(start_row, start_col, heading)
            maze.update_position(start_row, start_col)
            print("start_row =", start_row, "start_col =", start_col)
        elif cmd == "e":
            print("Ende - du kannst das Turtle-Fenster jetzt schließen")
        else:
            print("Unbekanntes Kommando")
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
