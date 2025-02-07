import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_rectangle(x, y, width, height):
    glBegin(GL_LINE_LOOP)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(1.0, 1.0, 1.0) 
    
    draw_rectangle(-0.5, -0.5, 1.0, 0.7)
    
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.6, 0.2)
    glVertex2f(0.6, 0.2)
    glVertex2f(0.0, 0.6)
    glEnd()
    
    draw_rectangle(-0.15, -0.5, 0.3, 0.4)
    
    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Render de casa")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glClearColor(0, 0, 0, 1) 
    glutMainLoop()

if __name__ == "__main__":
    main()
