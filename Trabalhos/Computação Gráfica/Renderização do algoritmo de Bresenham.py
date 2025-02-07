from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0, 0, 0, 1)
    glPointSize(5)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 10, 0, 10)

def render_line_bresenham():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    glColor3f(1, 1, 1)

    x1, y1 = 2, 3
    x2, y2 = 8, 6
    
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    
    x, y = x1, y1
    
    while True:
        glVertex2f(float(x), float(y))
        if x == x2 and y == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
    
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(300, 300)
    glutCreateWindow(b"Reta Bresenham")
    init()
    glutDisplayFunc(render_line_bresenham)
    glutMainLoop()

if __name__ == "__main__":
    main()
