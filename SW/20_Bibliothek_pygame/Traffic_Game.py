# Quelle: https://coderslegacy.com/python/python-pygame-tutorial/
# Geändert: Kommentiert
#           Variablen umbenannt
#           Bild-Dateien umbenannt
#           nur die notwendigen Farben definiert
#           score und speed sind Daten der Gegner-Klasse                      
#           neue Funktion end_of_game()
#           der Zusammenstoß wird 5 Sekunden lang angezeigt            
# Bibliotheken importieren
import pygame, sys
import random
import time
# alle Module initialisieren
pygame.init()
# Frames per second festlegen
FPS = 60
# Clock objekt erzeugen
FramePerSec = pygame.time.Clock()
# Breite und Höhe des Fensters festlegen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
# Farbe definieren
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
# Bild für den Hintergrund laden
background = pygame.image.load("animated_street.png")
# Schriften definieren
font_big = pygame.font.SysFont("Verdana", 40)
font_small = pygame.font.SysFont("Verdana", 20)
# Text definieren
meldung = font_big.render("Zusammenstoß", True, RED)
# Grafik-Fenster erzeugen
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen.fill(WHITE)
# Spieler-Klasse
class Player(pygame.sprite.Sprite):
    """Klasse für den Spieler"""
    def __init__(self):
        super().__init__()
        # Bild laden
        self.image = pygame.image.load("blue_car.png")
        # Rechteck in der Größe des Bildes erzeugen
        self.rect = self.image.get_rect()
        # Anfangsposition definieren
        self.rect.center = (160, 520)
    # Player bewegen    
    def move(self):
        # Zustand aller Tasten abfragen
        pressed_keys = pygame.key.get_pressed()
        # Wenn noch im Fenster: Player mit Taste steuern
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)
# Gegner-Klasse
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Bild laden
        self.image = pygame.image.load("red_car.png")
        # Rechteck in der Größe des Bildes erzeugen
        self.rect = self.image.get_rect()
        # zufällige Anfangsposition
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
        # score definieren
        self.score = 0
        # speed definieren
        self.speed = 5
    # Enemy bewegen
    def move(self):
        self.rect.move_ip(0,self.speed)
        # Wenn im Fenster unten angekommen
        if (self.rect.bottom > SCREEN_HEIGHT):
            # score erhöhen
            self.score += 1
            # oben im Fenster beginnen
            self.rect.top = 0
            # zufällige Anfangsposition
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    # score zeichnen
    def draw_score(self, surface):
        my_score = font_small.render(str(self.score), True, BLACK)
        surface.blit(my_score, (10,10))
# Instanzen erzeugen
P1 = Player()
E1 = Enemy()
# Gegner-Gruppe erzeugen
enemies = pygame.sprite.Group()
enemies.add(E1)
 # Gruppe mit Spieler und Gegner
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
# User-Ereignis INC_SPEED: eindeutige ID definieren
INC_SPEED = pygame.USEREVENT + 1 
# User-Ereignis alle 1000 Millisekunden erscheinen lassen
pygame.time.set_timer(INC_SPEED, 1000)
# Funktion beendet das Spiel
def end_of_game():
    # pygame Fenster schließen
    pygame.quit()
    # Python Skript beenden
    sys.exit()
#Game Loop
while True:  
    # Ereignisse prüfen  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            # Gegner schneller machen
            E1.speed += 1
        if event.type == pygame.QUIT:
            # Spiel-Ende
            end_of_game()
    # Straße zeichnen
    screen.blit(background, (0,0))
    # score zeichnen
    E1.draw_score(screen)
    # Spieler und Gegner bewegen und zeichnen
    for entity in all_sprites:
        # Spieler und Gegner bewegen
        entity.move()
        # Blocktransfer: source = entity.image, destination = entity.rect
        screen.blit(entity.image, entity.rect)
    # Zusammenstoß entdecken
    if pygame.sprite.spritecollideany(P1, enemies):
        # Sound abspielen
        pygame.mixer.Sound('crash.wav').play()
        # Zusammenstoß melden
        screen.blit(meldung, (30,250))
        # Grafik-Fenster aktualisieren
        pygame.display.update()
        # Warten
        time.sleep(5)
        # Spiel-Ende
        end_of_game()
    # Grafik-Fenster aktualisieren
    pygame.display.update()
    # Frames per second begrenzen
    FramePerSec.tick(FPS)
