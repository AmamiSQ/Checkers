import pygame

class Square:
    def __init__(self, color, posX, posY, side):
        self.color = color
        self.x = posX
        self.y = posY
        self.side = side
        self.side = side
    
    def drawSquare(self, screen):
        square = pygame.Rect(self.x, self.y, self.side, self.side)
        pygame.draw.rect(screen, self.color, square)