from turtle import Screen, Pen
from glob import glob
import os

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
        self.speed('fastest')

class Quadrado(Pen):
    forma = 'quadradoverde.gif'
    
    def __init__(self):
        super().__init__()
        self.shape(self.forma)
        self.up()
        self.speed('fastest')
        
class LogomarcaIF:
    topologia = [3,2,3,2]
    def __init__(self, x=0, y=0):
        self.xini = x
        self.yini = y
        self.imagens = [Bola()]
        for _ in range(sum(self.topologia)-1):
            self.imagens.append(Quadrado())
            
        self._posicionaimagens()
        
    def _posicionaimagens(self):
        i = 0
        for j,top in enumerate(self.topologia):
            y = self.yini -j*25
            for k in range(top):
                x = self.xini + k*25
                self.imagens[i].goto(x,y)
                i += 1
                
    def mover(self, x: int, y: int):
        self.xini = x
        self.yini = y
        self._posicionaimagens()
    


def main():
    tela = Screen()
    tela.setup(800,600)
    caminhoimgs = 'imagens'
    carregaimagens(caminhoimgs, tela)
#    bola = Bola()
#    quadrado = [Quadrado() for _ in range(9)]
#    for i in range(9):
#        q = 25*(i+1)
#        quadrado[i].goto(0,-q)
        
    logoif = LogomarcaIF()
    for i in range(4):
        logoif.mover(i*40, i*40)
        
    tela.exitonclick()

if __name__ == '__main__':
    main()


