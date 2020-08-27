# Detection-of-objects-with-Python-and-OpencV

## Criando amostra positiva

No terminal do windows você tem de colocar o seguinte comando para criar imagens positivas juntando a caneca com as imagens negativa em diversos angulos:


opencv_createsamples -img caneca01.jpg -bg negativas/bg.txt -info positivas/positivas.lst -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1800
-bgcolor 255


********************************************************************
## No arquivo lst na pasta positivas vai ter  a lista das imagens
ler da seguinte maneira:

o 1 indica que tem apenas uma caneca na imagem
depois vem a posição x(left)=10, y(top)=10, largura(width)=60, altura(height)=60                            
exemplo:
0001_0010_0010_0060_0060.jpg 1 10 10 60 60


********************************************************************
## Comando para gerar os vetores positivos:

opencv_createsamples -info positivas/positivas.lst -num 1800 -w 18 -h 18 -vec positivas.vec

*******************************************************************

## Comando cmd para treinar o classificador na pasta das negativas:


opencv_traincascade -data classificador -vec positivas.vec -bg bg.txt -numPos 1600 -numNeg 800 -numStages 10 -w 18 -h 18 -precalcBufSize 1024 -precalcIdxBufSize 1024

