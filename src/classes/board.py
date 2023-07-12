import pygame
from classes.square import Square

class Board:
    def __init__(self, sHeight, sWidth):
        self.side = 700
        self.rows = 8
        self.columns = 8
        self.color = (0,0,0)
        self.posX = ((sWidth / 2) - (self.side / 2))
        self.posY = ((sHeight / 2) - (self.side / 2))
    
    def drawBoard(self, screen):
        square = Square(self.color, self.posX, self.posY, self.side)
        square.drawSquare(screen)

        #add a border
        posX = self.posX - 25
        posY = self.posY - 25
        side = self.side + 50
        color = (255,215,0)

        border = Square(color, posX, posY, side)
        border.drawSquare(screen)

    def fillBoard(self, screen):
        white = (255,255,255)
        black = (0,0,0)

        #draw the squares
        for i in range(self.rows):
            for j in range(self.columns):
                posX = self.posX + (i * (self.side / self.rows))
                posY = self.posY + (j * (self.side / self.columns))
                size = (self.side / self.rows)

                if (i + j) % 2 == 0:
                    square = Square(white, posX, posY, size)
                    square.drawSquare(screen)
                else:
                    square = Square(black, posX, posY, size)
                    square.drawSquare(screen)
                
                    
