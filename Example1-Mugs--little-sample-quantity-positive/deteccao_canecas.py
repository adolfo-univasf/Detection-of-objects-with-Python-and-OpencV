import cv2

imagem = cv2.imread('Imagens teste canecas/teste01.png') #teste01
#imagem = cv2.imread('Imagens teste canecas/teste02.jpg') #teste02
#imagem = cv2.imread('Imagens teste canecas/teste03.jpg') #teste03
#imagem = cv2.imread('Imagens teste canecas/teste04.jpg') #teste04
#imagem = cv2.imread('Imagens teste canecas/teste05.jpg') #teste05
#imagem = cv2.imread('Imagens teste canecas/teste06.jpg') #teste06
#imagem = cv2.imread('Imagens teste canecas/teste07.jpg') #teste07
#imagem = cv2.imread('Imagens teste canecas/teste08.jpg') #teste08
#imagem = cv2.imread('Imagens teste canecas/teste09.jpg') #teste09
#imagem = cv2.imread('Imagens teste canecas/teste10.jpg') #teste10

classificador = cv2.CascadeClassifier('cascade_caneca1.xml')

imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

deteccoes = classificador.detectMultiScale(imagemcinza, scaleFactor=1.25, minNeighbors=3)

for (x,y,l,a)in deteccoes:
    cv2.rectangle(imagem, (x,y), (x + l, y + a), (0,255,0), 2)

cv2.imshow('Detector de Canecas',imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()