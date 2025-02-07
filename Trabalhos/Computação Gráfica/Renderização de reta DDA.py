import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0,0,0, 1)
    glPointSize(5)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,10,0,10)

def render_line_dda():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINE_STRIP)
    glColor3f(1,1,1)

    x1, y1 = 2,3
    x2, y2 = 8, 6
    step, k, dx, dy = 0,0,0,0
    inc_x, inc_y, x, y = 0,0,0,0
    
    dx = x2 - x1
    dy = y2 - y1

    if x1 == x2:
        dx = 1
    if y1 == y2:
        dy = 1

    if abs(dx) > abs(dy):
        step = abs(dx)
    else:
        step = abs(dy)

    inc_x = dx / step
    inc_y = dy / step

    x, y = x1, y1

    glVertex2f(float(x), float(y))
    for _ in range(1, step+1, 1):
        x = x + inc_x
        y = y + inc_y
        glVertex2f(float(x), float(y))
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(300, 300)
    glutCreateWindow(b"Reta DDA")
    init()
    glutDisplayFunc(render_line_dda)
    glutMainLoop()

if __name__ == "__main__":
    main()