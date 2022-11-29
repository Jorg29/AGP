import pygame
import pygame.freetype
import sys
import random
import copy
import os
from pygame import draw
from pygame import Rect as rect
from tkinter import *
from tkinter import simpledialog

#The number of living neighbors
def neighbors(squares, i, j):
    n = 0
    if i - 1 >= 0 and j - 1 >= 0 and squares[i - 1][j - 1]:
        n += 1
    if j - 1 >= 0 and squares[i][j - 1]:
        n += 1
    if i + 1 < len(squares) and j - 1 >= 0 and squares[i + 1][j - 1]:
        n += 1
    if i + 1 < len(squares) and squares[i + 1][j]:
        n += 1
    if i + 1 < len(squares) and j + 1 < len(squares[0]) and squares[i + 1][j + 1]:
        n += 1
    if j + 1 < len(squares[0]) and squares[i][j + 1]:
        n += 1
    if i - 1 >= 0 and j + 1 < len(squares[0]) and squares[i - 1][j + 1]:
        n += 1
    if i - 1 >= 0 and squares[i - 1][j]:
        n += 1
    return n

#Game of life rules
def process(squares):
    new_squares = copy.deepcopy(squares)
    for i in range(len(squares)):
        for j in range(len(squares[0])):
            num_neighbors = neighbors(squares, i, j)
            if squares[i][j] == True and num_neighbors != 2 and num_neighbors != 3:
                new_squares[i][j] = False
            if num_neighbors == 3 and not squares[i][j]:
                new_squares[i][j] = True
    return new_squares

#Random
def random_squares(spawn_rate):
    for i in range(len(squares)):
        for j in range(len(squares[0])):
            squares[i][j] = not bool(random.randint(0, spawn_rate))

#Windows of controls and inports
def printS():
    label = Label(root, text= "\nWelcome to Game of Life\n\n Let me show your controls\n"
                              "The Upper arrow (^) of the keyboard is being pressed is the automatic execution of steps\n"
                              "The Down arrow (˅) of the keyboard is being pressed is the automatic execution of steps is being paused\n"
                              "The Right arrow (>) of the keyboard is being pressed is to go one step further\n"
                              "The Left arrow (<) of the keyboard is being pressed is to take a step back when it was saved\n"
                              "The Tab buttom (Tab) of the keyboard is being pressed is to save the board\n\n")
    label.pack()

root = Tk()
root.title('Controls')
root.eval('tk::PlaceWindow . center')
button = Button(root, text="Controls", command=printS)
button.pack()

root.mainloop()

root1 = Tk()
root1.eval('tk::PlaceWindow . rigth')
root1.withdraw()
width = simpledialog.askinteger(title="Width",prompt="                           Chose your width:\n"
                                                 "(width/(scale=10) for example 20/10=2 =>width)\n")
height = simpledialog.askinteger(title="Height",prompt="                           Chose your height:\n"
                                                  "(height/(scale=10) for example 40/10=4 =>height)\n")
rand = simpledialog.askinteger(title="Random",prompt="Chose your probability of the initial activation of each cell:\n")

os.environ["SDL_VIDEO_CENTERED"] = '1'

scale = 10
width = width
height = height
framerate = 60

pygame.init()
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()

dodgerblue4 = 16,78,139
white = 255, 255, 255
black = 0, 0, 0
dodgerblue3 = 24,116,205

#The x and y directions
num_x = int(width / scale)
num_y = int(height / scale)

#Game state
squares = [[0] * num_y for _ in range(num_x)]

#Squares for the quick save
saved_squares = [[0] * num_y for _ in range(num_x)]

screen = pygame.display.set_mode((width, height))

run = False
frame = 0
gridlines = True
random_squares(rand)

while True:
    frame += 1
    if run:
        squares = process(squares)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            #Play
            if event.key == pygame.K_UP:
                run = not run
            #Pause
            if event.key == pygame.K_DOWN:
                run = not run
            #Next frame
            if event.key == pygame.K_RIGHT:
                squares = process(squares)

            #Quick save
            if event.key == pygame.K_TAB:
                saved_squares = copy.deepcopy(squares)

            #Quick load
            if event.key == pygame.K_LEFT:
                squares = copy.deepcopy(saved_squares)

            #Quit
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    #Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    screen.fill(white)

    # Draw gridlines
    if gridlines:
        for i in range(len(squares) + 1):
            draw.line(screen, black, (i * scale, 0), (i * scale, height))
        for i in range(len(squares[0]) + 1):
            draw.line(screen, black, (0, i * scale), (width, i * scale))

    #Draw squares
    for i in range(len(squares)):
        for j in range(len(squares[0])):
            if squares[i][j]:
                draw.rect(screen, dodgerblue4 , rect(i * scale, j * scale, scale, scale))

    #Highlight cell
    if not run:
        i = int(mouse_pos[0] / scale)
        j = int(mouse_pos[1] / scale)
        if squares[i][j]:
            draw.rect(screen, dodgerblue3,
                      rect(int(mouse_pos[0] / scale) * scale, int(mouse_pos[1] / scale) * scale, scale, scale))
        else:
            draw.rect(screen, black,
                      rect(int(mouse_pos[0] / scale) * scale, int(mouse_pos[1] / scale) * scale, scale, scale))

    pygame.display.update()