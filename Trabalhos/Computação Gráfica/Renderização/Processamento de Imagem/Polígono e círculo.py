import cv2
import numpy as np

img = cv2.imread('C:/Users/Naylan/Test.png')

altura, largura, _ = img.shape

pontos = np.array([[100 + 50, 50], [200 + 50, 50], [250 + 50, 150], 
                   [150 + 50, 200], [50 + 50, 150]], np.int32)

cv2.polylines(img, [pontos], isClosed=True, color=(0, 255, 0), thickness=2)

centro_x, centro_y = largura // 2, altura // 2
cv2.circle(img, (centro_x, centro_y), 20, (255, 255, 255), thickness=-1) 

cv2.imshow('Imagem com poligono e circulo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
