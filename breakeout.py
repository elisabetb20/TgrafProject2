print("hello world")

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
from random import *



x_pos = 300
y_pos = 50
going_right = False
going_left = False


def init_game():
    pygame.display.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF|OPENGL) #800 pixels wide and 600 pixels high
    glClearColor(0.0, 0.0, 0.0, 1.0)


def update():
    global x_pos
    global y_pos
    global going_left
    global going_right
    if going_left:
        x_pos -= 0.5
    if going_right:
        x_pos += 0.5

    if x_pos >= 650:
       going_right = False
    if x_pos <=0:
        going_left = False
          


def display():

    #the paddle
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, 800, 600)
    gluOrtho2D(0, 800, 0, 600)

   
    glBegin(GL_TRIANGLES)
    glVertex2f(x_pos, y_pos)
    glVertex2f(x_pos, y_pos + 10)
    glVertex2f(x_pos + 150, y_pos)

    glVertex2f(x_pos + 150, y_pos + 10)
    glVertex2f(x_pos, y_pos + 10)
    glVertex2f(x_pos + 150, y_pos)

    glEnd()

    


    pygame.display.flip()

def game_loop():
    global x_pos
    global y_pos
    global going_right
    global going_left

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:

                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == K_q:
                    glClearColor(random(), random(), random(), 1.0)
                elif event.key == K_LEFT:
                    going_left = True
                elif event.key == K_RIGHT:
                    going_right = True
            elif event.type == pygame.KEYUP:
                if event.key == K_LEFT:
                   going_left = False
                if event.key == K_RIGHT:
                    going_right = False
            
    update()
    display()

if __name__ == "__main__":
    init_game()
    while True:
        game_loop()





