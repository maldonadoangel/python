import pygame
import random

class Cuerpo:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direccion = 0
        self.ventana = ventana
    def dibujar(self):
        pygame.draw.rect(self.ventana, (255, 255, 255), (self.x, self.y, 10, 10))

class Manzanas:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.ventana = ventana
    def dibujar(self):
        pygame.draw.rect(self.ventana, (255, 0, 0), (self.x, self.y, 10, 10))
        
    
        
def refrescar(ventana):
    ventana.fill((0, 0, 0))
    comida.dibujar()
    for i in range(len(serpiente)):
        serpiente[i].dibujar()
    
def main():
    global serpiente, comida
    ventana = pygame.display.set_mode((500, 500))
    ventana.fill((0, 0, 0))
    comida = manzanas(ventana)
    serpiente = [cuerpo(ventana)]
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        refrescar(ventana)

if __name__ == '  main  ':
    main()
    pygame.quit()
    