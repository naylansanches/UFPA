from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window_height = 500
window_width = 500
window_title = b"Render de reta analitica"
x = [0.0] * 7
y = [0.0] * 7

def funcao_reta_analitica(x, y):
    pontos = []
    
    for i in range(6):
        x1, y1 = x[i], y[i]
        x2, y2 = x[i+1], y[i+1]
        
        if x1 > x2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        if x1 == x2:
            y_min, y_max = min(y1, y2), max(y1, y2)
            y_val = y_min
            while y_val <= y_max:
                pontos.append((x1, y_val))
                y_val += 0.01 
        else:
            m = (y2 - y1) / (x2 - x1)
            b = y1 - m * x1
            x_val = x1
            while x_val <= x2:
                y_val = m * x_val + b
                pontos.append((x_val, y_val))
                x_val += 0.01 
    
    glBegin(GL_POINTS)
    for px, py in pontos:
        glVertex2f(px, py)
    glEnd()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 10, 0, 10)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    funcao_reta_analitica(x, y)
    glFlush()

def main():
    global x, y
    print("Você precisa inserir as coordernadas para desenhar as linhas.")
    
    for i in range(7):
        # Converte para inteiro após leitura
        x[i] = int(float(input(f"Insira o valor de x{i+1}: ")))
        y[i] = int(float(input(f"Insira o valor de y{i+1}: ")))

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow(window_title)
    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()