from turtle import Screen, Pen
from glob import glob
import os
from math import sin,cos, pi
import time

def carregaimagens(caminho: str, tela: Screen) -> None:
    pastaatual = os.getcwd()
    os.chdir(caminho)
    imagens = glob('*.gif')
    for img in imagens:
        tela.addshape(img)
        
    os.chdir(pastaatual)

class Bola(Pen):
    forma = 'bolavermelha.gif'
    
    def __init__(self):
        super().__init__()
        self.shape(self.forma)
        self.up()
        #self.speed('fast')

class Quadrado(Pen):
    forma = 'quadradoverde.gif'
    
    def __init__(self):
        super().__init__()
        self.shape(self.forma)
        self.up()
        #self.speed('fast')
        
class LogomarcaIF:
    topologia = [3,2,3,2]
    def __init__(self, x=0, y=0):
        self.xini = x
        self.yini = y
        self._imagens = [Bola()]
        for _ in range(sum(self.topologia)-1):
            self._imagens.append(Quadrado())
            
        self.arrumar()
        
    def arrumar(self):
        i = 0
        for j,top in enumerate(self.topologia):
            y = self.yini -j*25
            for k in range(top):
                x = self.xini + k*25
                self._imagens[i].goto(x,y)
                i += 1
                
    def mover(self, x: int, y: int):
        dx = x - self.xini
        dy = y - self.yini
        self.xini = x
        self.yini = y
        for img in self._imagens:
            cx,cy = img.position()
            img.goto(cx+dx, cy+dy)
     
    # Espalha as imagens de maneira radial       
    def espalhar(self, raio=30):
        qtimgs = len(self._imagens)
        esp_angular = 360/qtimgs
        for k, img in enumerate(self._imagens):
            ang = k*esp_angular*pi/180
            img.goto(raio*cos(ang)+self.xini,
                     raio*sin(ang)+self.yini)
            #img.stamp()

    # Espalha as imagens de maneira radial       
    def espalhar2(self, raio=30):
        qtimgs = len(self._imagens)-1
        esp_angular = 360/qtimgs
        for k, img in enumerate(self._imagens[1:]):
            ang = k*esp_angular*pi/180
            img.goto(raio*cos(ang)+self.xini,
                     raio*sin(ang)+self.yini)
            #img.stamp()

                     
    def girar(self):
        xa,ya = self._imagens[-1].position()
        for i,img in enumerate(self._imagens):
            xb,yb = img.position()
            img.goto(xa,ya)
            xa,ya = xb,yb

    def girar2(self):
        xa,ya = self._imagens[-1].position()
        for i,img in enumerate(self._imagens[1:]):
            xb,yb = img.position()
            img.goto(xa,ya)
            xa,ya = xb,yb
            
    def cobrinha(self):
        y = self.yini
        for i,img in enumerate(self._imagens):
            x = self.xini + i*25
            self._imagens[i].goto(x,y)
            
class CantoIF:
    topologia = {'se':[3,2,1],
                 'sd':[-3,-2,-1],
                 'ie':[1,2,3],
                 'id':[-1,-2,-3]}
    def __init__(self, x=0, y=0, canto='se'):
        self.xini = x
        self.yini = y
        self.canto = canto
        self._imagens = [Quadrado() for _ in range(abs(sum(self.topologia[canto])))]
        self.arrumar()
        
    def arrumar(self):
        i = 0
        qtlinha0 = self.topologia[self.canto][0]
        sinal = qtlinha0//abs(qtlinha0)
        for j,top in enumerate(self.topologia[self.canto]):
            y = self.yini -j*25
            for k in range(sinal*top):
                x = self.xini + sinal*k*25
                self._imagens[i].goto(x,y)
                i += 1     


def main():
    tela = Screen()
    tela.setup(800,600)
    tela.title('Animação com Logomarca do IF')
    caminhoimgs = 'imagens'
    carregaimagens(caminhoimgs, tela)
    #time.sleep(10)
#    bola = Bola()
#    quadrado = [Quadrado() for _ in range(9)]
#    for i in range(9):
#        q = 25*(i+1)
#        quadrado[i].goto(0,-q)
    cantose = CantoIF(x=-350,y=250,canto='se')
    cantoie = CantoIF(x=-350,y=-200,canto='ie')
    cantose = CantoIF(x=350,y=250,canto='sd')
    cantoie = CantoIF(x=350,y=-200,canto='id')
    logoif = LogomarcaIF()
    
    for i in range(4):
        logoif.mover(i*40, i*40)
        
    logoif.mover(0,0)
    
    for j in range(19):
        logoif.espalhar2(15*j)

    for i in range(9):
        logoif.girar2()
         
    for k in range(19,0,-1):
        logoif.espalhar2(15*k)
        
    logoif.arrumar()
    
    tela.exitonclick()


if __name__ == '__main__':
    main()
