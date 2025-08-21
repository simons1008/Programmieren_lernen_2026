# Programm erzeugt ein fenster mit einem Auto und Gegenverkehr
# - Das eine Auto wird mit den Pfeil-Tasten gesteuert
# - Das andere Auto kommt auf einem zufälligen Kurs entgegen
# Bibliotheken importieren
import pygame, sys
import random
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
    # Player zeichnen            
    def draw(self, surface):
        # Blocktransfer: source = self.image, destination = self.rect
        surface.blit(self.image, self.rect)      
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
    # Enemy bewegen
    def move(self):
        self.rect.move_ip(0,10)
        # Wenn im Fenster unten angekommen
        if (self.rect.bottom > SCREEN_HEIGHT):
            # oben im Fenster beginnen
            self.rect.top = 0
            # zufällige Anfangsposition
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    # Gegner zeichnen 
    def draw(self, surface):
        # Blocktransfer: source = self.image, destination = self.rect
        surface.blit(self.image, self.rect)      
# Instanzen erzeugen
P1 = Player()
E1 = Enemy()
#Game Loop
while True:  
    # Ereignisse prüfen  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # pygame Fenster schließen
            pygame.quit()
            # Python Skript beenden
            sys.exit()
    # Player bewegen
    P1.move()
    # Enemy bewegen
    E1.move()
    # Grafik-Fenster auswischen
    screen.fill(WHITE)
    # Player zeichnen
    P1.draw(screen)
    # Enemy zeichnen
    E1.draw(screen)
    # Grafik-Fenster aktualisieren
    pygame.display.update()
    # Frames per second begrenzen
    FramePerSec.tick(FPS)
