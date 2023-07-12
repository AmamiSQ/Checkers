import pygame
from classes.board import Board

pygame.init()


# Create the screen
width = 800
height = 800
screen = pygame.display.set_mode((width, height))

# Title and Icon
pygame.display.set_caption("Checkers")
icon = pygame.image.load("./assets/icon.png")
pygame.display.set_icon(icon)





# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #don't put shit above screen.fill, it'll be covered up
    screen.fill((0, 0, 0))

    #draw the main board
    board = Board(height, width)
    board.drawBoard(screen)
    board.fillBoard(screen)





    pygame.display.update()
